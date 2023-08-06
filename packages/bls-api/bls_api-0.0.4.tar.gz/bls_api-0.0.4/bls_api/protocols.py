from pydantic import BaseModel,StrictStr
from typing import List, Union
class series_list(BaseModel):
    series: Union[List[StrictStr],StrictStr]
class series_id(BaseModel):
    id:StrictStr





