from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union

from .types import (AttachStorage, BlockStorage, StorageRequest, VMInstance,
                    DNSRecord, DNSZone,
                    VMRequest)


class ProviderSpec(ABC):
    """Interface definition of a cloud provider"""
    providerid: str

    @abstractmethod
    def get_vm(self, vm_name: str, location: Optional[str] = None) \
            -> VMInstance:
        pass

    @abstractmethod
    def create_vm(self, vm: VMRequest) -> VMInstance:
        pass

    @abstractmethod
    def destroy_vm(self, vm: Union[str, VMInstance],
                   location: Optional[str] = None):
        pass

    @abstractmethod
    def list_vms(
        self, location: Optional[str] = None, tags: Optional[List[str]] = None
    ) -> List[VMInstance]:
        pass

    @abstractmethod
    def get_volume(self, vol_name) -> BlockStorage:
        pass

    @abstractmethod
    def create_volume(self, disk: StorageRequest) -> BlockStorage:
        pass

    @abstractmethod
    def destroy_volume(self, disk: str, location: Optional[str] = None) -> bool:
        pass

    @abstractmethod
    def attach_volume(self, vm: str, attach: AttachStorage,
                      location: Optional[str] = None) -> bool:
        pass

    @abstractmethod
    def detach_volume(self, vm: str, disk: str,
                      location: Optional[str] = None) -> bool:
        pass

    @abstractmethod
    def list_volumes(self, location: Optional[str] = None) \
            -> List[BlockStorage]:
        pass


class DNSSpec(ABC):

    def get_zone(self, zoneid: str):
        pass

    def create_zone(self, zone: DNSZone):
        pass

    def create_record(self, record: DNSRecord) -> Dict[str, Any]:
        pass

    def delete_zone(self, zoneid: str):
        pass

    def delete_record(self, zoneid: str, recordid: str) -> bool:
        pass
