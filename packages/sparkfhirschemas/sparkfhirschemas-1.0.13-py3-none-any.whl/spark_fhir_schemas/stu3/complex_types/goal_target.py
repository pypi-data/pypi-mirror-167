from typing import Union, List, Optional

from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    ArrayType,
    DateType,
    DataType,
)


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class Goal_TargetSchema:
    """
    Describes the intended objective(s) for a patient, group or organization care,
    for example, weight loss, restoring an activity of daily living, obtaining
    herd immunity via immunization, meeting a process improvement objective, etc.
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
        Describes the intended objective(s) for a patient, group or organization care,
        for example, weight loss, restoring an activity of daily living, obtaining
        herd immunity via immunization, meeting a process improvement objective, etc.


        id: unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. In order to make the use of extensions safe and
            manageable, there is a strict set of governance  applied to the definition and
            use of extensions. Though any implementer is allowed to define an extension,
            there is a set of requirements that SHALL be met as part of the definition of
            the extension.

        measure: The parameter whose value is being tracked, e.g. body weight, blood pressure,
            or hemoglobin A1c level.

        detailQuantity: The target value of the focus to be achieved to signify the fulfillment of the
            goal, e.g. 150 pounds, 7.0%. Either the high or low or both values of the
            range can be specified. When a low value is missing, it indicates that the
            goal is achieved at any focus value at or below the high value. Similarly, if
            the high value is missing, it indicates that the goal is achieved at any focus
            value at or above the low value.

        detailRange: The target value of the focus to be achieved to signify the fulfillment of the
            goal, e.g. 150 pounds, 7.0%. Either the high or low or both values of the
            range can be specified. When a low value is missing, it indicates that the
            goal is achieved at any focus value at or below the high value. Similarly, if
            the high value is missing, it indicates that the goal is achieved at any focus
            value at or above the low value.

        detailCodeableConcept: The target value of the focus to be achieved to signify the fulfillment of the
            goal, e.g. 150 pounds, 7.0%. Either the high or low or both values of the
            range can be specified. When a low value is missing, it indicates that the
            goal is achieved at any focus value at or below the high value. Similarly, if
            the high value is missing, it indicates that the goal is achieved at any focus
            value at or above the low value.

        dueDate: Indicates either the date or the duration after start by which the goal should
            be met.

        dueDuration: Indicates either the date or the duration after start by which the goal should
            be met.

        """
        from spark_fhir_schemas.stu3.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.stu3.complex_types.codeableconcept import (
            CodeableConceptSchema,
        )
        from spark_fhir_schemas.stu3.complex_types.quantity import QuantitySchema
        from spark_fhir_schemas.stu3.complex_types.range import RangeSchema
        from spark_fhir_schemas.stu3.complex_types.duration import DurationSchema

        if (
            max_recursion_limit
            and nesting_list.count("Goal_Target") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Goal_Target"]
        schema = StructType(
            [
                # unique id for the element within a resource (for internal references). This
                # may be any string value that does not contain spaces.
                StructField("id", StringType(), True),
                # May be used to represent additional information that is not part of the basic
                # definition of the element. In order to make the use of extensions safe and
                # manageable, there is a strict set of governance  applied to the definition and
                # use of extensions. Though any implementer is allowed to define an extension,
                # there is a set of requirements that SHALL be met as part of the definition of
                # the extension.
                StructField(
                    "extension",
                    ArrayType(
                        ExtensionSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth,
                            max_extension_depth=max_extension_depth,
                        )
                    ),
                    True,
                ),
                # The parameter whose value is being tracked, e.g. body weight, blood pressure,
                # or hemoglobin A1c level.
                StructField(
                    "measure",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                    ),
                    True,
                ),
                # The target value of the focus to be achieved to signify the fulfillment of the
                # goal, e.g. 150 pounds, 7.0%. Either the high or low or both values of the
                # range can be specified. When a low value is missing, it indicates that the
                # goal is achieved at any focus value at or below the high value. Similarly, if
                # the high value is missing, it indicates that the goal is achieved at any focus
                # value at or above the low value.
                StructField(
                    "detailQuantity",
                    QuantitySchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                    ),
                    True,
                ),
                # The target value of the focus to be achieved to signify the fulfillment of the
                # goal, e.g. 150 pounds, 7.0%. Either the high or low or both values of the
                # range can be specified. When a low value is missing, it indicates that the
                # goal is achieved at any focus value at or below the high value. Similarly, if
                # the high value is missing, it indicates that the goal is achieved at any focus
                # value at or above the low value.
                StructField(
                    "detailRange",
                    RangeSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                    ),
                    True,
                ),
                # The target value of the focus to be achieved to signify the fulfillment of the
                # goal, e.g. 150 pounds, 7.0%. Either the high or low or both values of the
                # range can be specified. When a low value is missing, it indicates that the
                # goal is achieved at any focus value at or below the high value. Similarly, if
                # the high value is missing, it indicates that the goal is achieved at any focus
                # value at or above the low value.
                StructField(
                    "detailCodeableConcept",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                    ),
                    True,
                ),
                # Indicates either the date or the duration after start by which the goal should
                # be met.
                StructField("dueDate", DateType(), True),
                # Indicates either the date or the duration after start by which the goal should
                # be met.
                StructField(
                    "dueDuration",
                    DurationSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                    ),
                    True,
                ),
            ]
        )
        if not include_extension:
            schema.fields = [
                c
                if c.name != "extension"
                else StructField("extension", StringType(), True)
                for c in schema.fields
            ]

        return schema
