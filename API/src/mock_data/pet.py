from API.src.enums.common import Status
from API.src.mock_data.category import category
from API.src.mock_data.tag import tag
from API.src.models.pet_model import PetModel

create_pet_payload = PetModel(
    id=102569,
    category=category,
    name="Pet 1",
    photoUrls=["url"],
    tags=[tag],
    status=Status.Available
)

update_pet_payload = PetModel(
    id=102569,
    category=category,
    name="Pet updated",
    photoUrls=["url"],
    tags=[tag],
    status=Status.Available
)
