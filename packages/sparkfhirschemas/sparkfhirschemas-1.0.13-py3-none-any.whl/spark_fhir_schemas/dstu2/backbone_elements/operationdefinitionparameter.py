from typing import Union, List, Optional

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class OperationDefinitionParameterSchema:
    """
    A formal computable definition of an operation (on the RESTful interface) or a
    named query (using the search interaction).
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
        A formal computable definition of an operation (on the RESTful interface) or a
        named query (using the search interaction).


            id: None
            extension: May be used to represent additional information that is not part of the basic
        definition of the element. In order to make the use of extensions safe and
        manageable, there is a strict set of governance  applied to the definition and
        use of extensions. Though any implementer is allowed to define an extension,
        there is a set of requirements that SHALL be met as part of the definition of
        the extension.
            modifierExtension: May be used to represent additional information that is not part of the basic
        definition of the element, and that modifies the understanding of the element
        that contains it. Usually modifier elements provide negation or qualification.
        In order to make the use of extensions safe and manageable, there is a strict
        set of governance applied to the definition and use of extensions. Though any
        implementer is allowed to define an extension, there is a set of requirements
        that SHALL be met as part of the definition of the extension. Applications
        processing a resource are required to check for modifier extensions.
            name: The name of used to identify the parameter.
            use: Whether this is an input or an output parameter.
            min: The minimum number of times this parameter SHALL appear in the request or
        response.
            max: The maximum number of times this element is permitted to appear in the request
        or response.
            documentation: Describes the meaning or use of this parameter.
            type: The type for this parameter.
            profile: A profile the specifies the rules that this parameter must conform to.
            binding: Binds to a value set if this parameter is coded (code, Coding,
        CodeableConcept).
            part: The parts of a Tuple Parameter.
        """
        # id
        from spark_fhir_schemas.dstu2.simple_types.id import idSchema

        # extension
        from spark_fhir_schemas.dstu2.complex_types.extension import ExtensionSchema

        # name
        # type = code
        # min
        from spark_fhir_schemas.dstu2.simple_types.integer import integerSchema

        # profile
        from spark_fhir_schemas.dstu2.complex_types.reference import ReferenceSchema

        # binding
        from spark_fhir_schemas.dstu2.backbone_elements.operationdefinitionbinding import (
            OperationDefinitionBindingSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("OperationDefinitionParameter")
            >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["OperationDefinitionParameter"]
        schema = StructType(
            [
                # None
                StructField(
                    "id",
                    idSchema.get_schema(
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
                            extension_depth=extension_depth + 1,
                            max_extension_depth=max_extension_depth,
                        )
                    ),
                    True,
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the element, and that modifies the understanding of the element
                # that contains it. Usually modifier elements provide negation or qualification.
                # In order to make the use of extensions safe and manageable, there is a strict
                # set of governance applied to the definition and use of extensions. Though any
                # implementer is allowed to define an extension, there is a set of requirements
                # that SHALL be met as part of the definition of the extension. Applications
                # processing a resource are required to check for modifier extensions.
                StructField(
                    "modifierExtension",
                    ArrayType(
                        ExtensionSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth + 1,
                            max_extension_depth=max_extension_depth,
                        )
                    ),
                    True,
                ),
                # The name of used to identify the parameter.
                StructField("name", StringType(), True),
                # Whether this is an input or an output parameter.
                StructField("use", StringType(), True),
                # The minimum number of times this parameter SHALL appear in the request or
                # response.
                StructField(
                    "min",
                    integerSchema.get_schema(
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
                # The maximum number of times this element is permitted to appear in the request
                # or response.
                StructField("max", StringType(), True),
                # Describes the meaning or use of this parameter.
                StructField("documentation", StringType(), True),
                # The type for this parameter.
                StructField("type", StringType(), True),
                # A profile the specifies the rules that this parameter must conform to.
                StructField(
                    "profile",
                    ReferenceSchema.get_schema(
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
                # Binds to a value set if this parameter is coded (code, Coding,
                # CodeableConcept).
                StructField(
                    "binding",
                    OperationDefinitionBindingSchema.get_schema(
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
                # The parts of a Tuple Parameter.
                StructField(
                    "part",
                    ArrayType(
                        OperationDefinitionParameterSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth + 1,
                            max_extension_depth=max_extension_depth,
                        )
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
