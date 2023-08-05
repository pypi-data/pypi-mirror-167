from typing import Union, List, Optional

from pyspark.sql.types import StructType, StringType, DataType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class instantSchema:
    """
    An instant in time - known at least to the second
    Note: This is intended for precisely observed times, typically system logs
    etc., and not human-reported times - for them, see date and dateTime below.
    Time zone is always required
    If the element is present, it must have either a @value, an @id, or extensions
    """

    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(
        max_nesting_depth: Optional[int] = 6,
        nesting_depth: int = 0,
        nesting_list: List[str] = [],
        max_recursion_limit: Optional[int] = 2,
        include_extension: Optional[bool] = False,
        extension_fields: Optional[List[str]] = [
            "valueBoolean",
            "valueCode",
            "valueDate",
            "valueDateTime",
            "valueDecimal",
            "valueId",
            "valueInteger",
            "valuePositiveInt",
            "valueString",
            "valueTime",
            "valueUnsignedInt",
            "valueUri",
            "valueQuantity",
        ],
        extension_depth: int = 0,
        max_extension_depth: Optional[int] = 2,
    ) -> Union[StructType, DataType]:
        """
        An instant in time - known at least to the second
        Note: This is intended for precisely observed times, typically system logs
        etc., and not human-reported times - for them, see date and dateTime below.
        Time zone is always required
        If the element is present, it must have either a @value, an @id, or extensions


        """
        return StringType()
