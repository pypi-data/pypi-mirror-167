# coding=utf-8
# Copyright 2022 The TensorFlow Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""DatasetCollection base class."""
import dataclasses
import inspect
from typing import Any, List, Mapping, Optional, Type, Union

from etils import epath
from tensorflow_datasets.core import naming
from tensorflow_datasets.core import registered
from tensorflow_datasets.core.utils import version as version_lib

DESCRIPTION_FILE = "description.md"
CITATIONS_FILE = "citations.bib"


def get_filepath_in_dataset_folder(dataset_cls: Type[Any],
                                   file_name: str) -> epath.Path:
  directory_path = epath.Path(inspect.getfile(dataset_cls)).parent
  return directory_path / file_name


def get_file_content_from_dataset_folder(
    dataset_class: Type[Any],
    file_name: str,
    raise_error_if_fails: bool = False,
) -> Optional[str]:
  """Returns the file content from the relevant dataset folder.

  Args:
    dataset_class: The dataset collection class for which the file has to be
      read.
    file_name: The name of the file to load.
    raise_error_if_fails: Whether to raise an error if the file's content cannot
      be retrieved.

  Returns:
    The requested file's content. If unavailable, it will return None if
    raise_error_if_fails is set to False, otherwise it will raise the
    encountered error.
  """
  file_path = get_filepath_in_dataset_folder(dataset_class, file_name)
  try:
    return file_path.read_text()
  except Exception as e:  # pylint: disable=broad-except
    if raise_error_if_fails:
      raise e
    else:
      return None


@dataclasses.dataclass
class DatasetCollectionInfo:
  """Information about a dataset collection.

  `DatasetCollectionInfo` documents a dataset collection, including its name,
  description, release notes and citations.

  Attributes:
    name: The name of the dataset collection.
    description: A markdown-formatted description of the dataset collection.
    release_notes: A mapping of dataset collection's versions with their
      corresponding release notes.
    citation: Optional citation for the dataset collection.
  """

  name: str
  description: str
  release_notes: Mapping[str, str]
  citation: Optional[str] = None

  @classmethod
  def from_cls(cls,
               dataset_collection_class: Type["DatasetCollection"],
               release_notes: Mapping[str, str],
               description: Optional[str] = None,
               citation: Optional[str] = None) -> "DatasetCollectionInfo":
    """Creates a DatasetCollectionInfo instance based on class information."""
    name: str = naming.camelcase_to_snakecase(dataset_collection_class.__name__)
    if not description:
      description = get_file_content_from_dataset_folder(
          dataset_collection_class, DESCRIPTION_FILE, raise_error_if_fails=True)
    if not citation:
      citation = get_file_content_from_dataset_folder(dataset_collection_class,
                                                      CITATIONS_FILE)
    return cls(
        name=name,
        release_notes=release_notes,
        description=description,
        citation=citation)


@dataclasses.dataclass
class DatasetReference:
  """Reference to a dataset.

  Attributes:
    dataset_name: name of the dataset.
    version: version of the dataset to be used. If `None`, the latest version
      will be loaded. An error is raised if the specified version cannot be
      provided.
    split_mapping: mapping between split names. If the `DatasetCollection` wants
      to use different split names than the source datasets, then this mapping
      can be used. For example, if the collection uses the split `valid`, but
      this dataset uses the split `validation`, then the `split_mapping` should
      be `{'validation': 'valid'}`.
    config: optional config to be used in the dataset.
  """
  dataset_name: str
  version: Union[None, str, version_lib.Version] = None
  split_mapping: Optional[Mapping[str, str]] = None
  config: Optional[str] = None

  def __post_init__(self):
    if isinstance(self.version, str):
      self.version = version_lib.Version(self.version)

  def tfds_name(self) -> str:
    """Returns the TFDS name of the referenced dataset."""
    dataset_name = self.dataset_name
    if self.config:
      dataset_name += f"/{self.config}"
    if self.version:
      dataset_name += f":{self.version}"
    return dataset_name

  def get_split(self, split: str) -> str:
    if self.split_mapping:
      return self.split_mapping.get(split, split)
    return split

  @classmethod
  def from_tfds_name(
      cls,
      tfds_name: str,
      split_mapping: Optional[Mapping[str, str]] = None,
  ) -> "DatasetReference":
    """Returns the `DatasetReference` for the given TFDS dataset."""
    parsed_name, builder_kwargs = naming.parse_builder_name_kwargs(tfds_name)
    version, config = None, None
    version = builder_kwargs.get("version")
    config = builder_kwargs.get("config")
    return cls(
        dataset_name=parsed_name.name,
        version=version,
        config=config,
        split_mapping=split_mapping)


def references_for(
    name_to_tfds_name: Mapping[str, str]) -> Mapping[str, DatasetReference]:
  """Constructs of dataset references.

  Note that you can specify the config and the version in the TFDS name.
  For example:
  ```
  references_for(name_to_tfds_name={
    "wiki_it": "wikipedia/20201201.it:1.0.0",
    "wiki_en": "scan/length:1.1.1",
  })
  ```

  Args:
    name_to_tfds_name: The mapping between name to be used in the dataset
      collection and the TFDS name (plus optional config and version).

  Returns:
    Returns a dictionary of dataset_name: `DatasetReference`.
  """
  return {
      name: DatasetReference.from_tfds_name(tfds_name)
      for name, tfds_name in name_to_tfds_name.items()
  }


def reference_for(tfds_name: str) -> DatasetReference:
  """Returns the corresponding `DatasetReference` for a TFDS dataset name."""
  return DatasetReference.from_tfds_name(tfds_name)


class DatasetCollection(
    registered.RegisteredDatasetCollection, skip_registration=True):
  """Base class to define a dataset collection.

  Subclasses should overwrite `info` to return populated DatasetCollectionInfo.

  Subclasses should also overwrite `datasets` to return a dictionary of versions
  to the datasets included in that collection's version.
  """

  @property
  def info(self) -> DatasetCollectionInfo:
    raise NotImplementedError

  @property
  def datasets(self) -> Mapping[str, Mapping[str, DatasetReference]]:
    """Returns the datasets included in the collection, ordered by version.

    Users will need to overwrite this function when implementing their dataset
    collection.

    The returned dictionary needs to contain the dataset collection versions as
    keys, and a dictionary of the included TFDS datasets as values.

    For example:
    ```
    @property
    def datasets(self):
    return {
        "1.0.0":
            dataset_collection_builder.references_for({
                "yes_no": "yes_no:1.0.0",
                "sst2": "glue/sst:2.0.0",
                "assin2": "assin2:1.0.0",
            }),
        ...
    }
    ```

    Note that the above is equivalent to:
    ```
    @property
    def datasets(self):
    return {
        "1.0.0": {
            "yes_no":
                dataset_collection_builder.DatasetReference(
                    dataset_name="yes_no", version="1.0.0"),
            "sst2":
                dataset_collection_builder.DatasetReference(
                    dataset_name="glue", config="sst2", version="2.0.0"),
            "assin2":
                dataset_collection_builder.DatasetReference(
                    dataset_name="assin2", version="1.0.0"),
        },
        ...
    }
    ```
    """
    raise NotImplementedError

  def __repr__(self):
    return (f"DatasetCollection(info={self.info}, "
            f"datasets={self.datasets})")

  @property
  def all_versions(self) -> List[version_lib.Version]:
    """Returns all versions available for the dataset collection."""
    return [
        version_lib.Version(version_str)
        for version_str in self.datasets.keys()
    ]

  def get_latest_version(self) -> str:
    """Returns the latest version of this dataset collection."""
    return str(max(self.all_versions))

  def get_collection(
      self,
      version: Union[None, str, version_lib.Version] = None,
  ) -> Mapping[str, DatasetReference]:
    """Returns the requested versioned dataset collection.

    Args:
      version: The requested version. If no version is specified, returns the
        most recently added version.

    Returns:
      The requested dataset collection.
    """
    if not version:
      return self.datasets[self.get_latest_version()]

    if isinstance(version, version_lib.Version):
      version = str(version)
    for v in reversed(self.all_versions):
      if v.match(version):
        return self.datasets[str(v)]

    raise ValueError(f"No datasets could be retrieved for version {version}")

  def list_datasets(
      self,
      version: Union[None, str, version_lib.Version] = None,
  ) -> str:
    """Returns the datasets included in a versioned dataset collection."""
    msgs = [f"The dataset collection {self.info.name}"]
    if version:
      msgs.append(f"(version: {version})")
    msgs.append("contains the datasets:\n")
    versioned_collection = self.get_collection(version)
    for ds_name, benchmark_spec in versioned_collection.items():
      msgs.append(f"- {ds_name}: {benchmark_spec}\n")
    return " ".join(msgs)
