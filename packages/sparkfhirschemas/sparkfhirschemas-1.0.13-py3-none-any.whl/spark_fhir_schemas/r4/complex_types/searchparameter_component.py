from typing import Union, List, Optional

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType


# This file is auto-generated by generate_schema so do not edit it manually
# noinspection PyPep8Naming
class SearchParameter_ComponentSchema:
    """
    A search parameter that defines a named search item that can be used to
    search/filter on a resource.
    """

    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(
        max_nesting_depth: Optional[int] = 6,
        nesting_depth: int = 0,
        nesting_list: List[str] = [],
        max_recursion_limit: Optional[int] = 2,
        include_extension: Optional[bool] = False,
        extension_fields: Optional[List[str]] = None,
        extension_depth: int = 0,
        max_extension_depth: Optional[int] = 2,
        include_modifierExtension: Optional[bool] = False,
        use_date_for: Optional[List[str]] = None,
        parent_path: Optional[str] = "",
    ) -> Union[StructType, DataType]:
        """
        A search parameter that defines a named search item that can be used to
        search/filter on a resource.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        modifierExtension: May be used to represent additional information that is not part of the basic
            definition of the element and that modifies the understanding of the element
            in which it is contained and/or the understanding of the containing element's
            descendants. Usually modifier elements provide negation or qualification. To
            make the use of extensions safe and manageable, there is a strict set of
            governance applied to the definition and use of extensions. Though any
            implementer can define an extension, there is a set of requirements that SHALL
            be met as part of the definition of the extension. Applications processing a
            resource are required to check for modifier extensions.

            Modifier extensions SHALL NOT change the meaning of any elements on Resource
            or DomainResource (including cannot change the meaning of modifierExtension
            itself).

        definition: The definition of the search parameter that describes this part.

        expression: A sub-expression that defines how to extract values for this component from
            the output of the main SearchParameter.expression.

        """
        if extension_fields is None:
            extension_fields = [
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
                "valueUrl",
                "valueReference",
                "valueCodeableConcept",
                "valueAddress",
            ]
        from spark_fhir_schemas.r4.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.r4.simple_types.canonical import canonicalSchema

        if (
            max_recursion_limit
            and nesting_list.count("SearchParameter_Component") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["SearchParameter_Component"]
        my_parent_path = (
            parent_path + ".searchparameter_component"
            if parent_path
            else "searchparameter_component"
        )
        schema = StructType(
            [
                # Unique id for the element within a resource (for internal references). This
                # may be any string value that does not contain spaces.
                StructField("id", StringType(), True),
                # May be used to represent additional information that is not part of the basic
                # definition of the element. To make the use of extensions safe and manageable,
                # there is a strict set of governance  applied to the definition and use of
                # extensions. Though any implementer can define an extension, there is a set of
                # requirements that SHALL be met as part of the definition of the extension.
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
                            include_modifierExtension=include_modifierExtension,
                            use_date_for=use_date_for,
                            parent_path=my_parent_path,
                        )
                    ),
                    True,
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the element and that modifies the understanding of the element
                # in which it is contained and/or the understanding of the containing element's
                # descendants. Usually modifier elements provide negation or qualification. To
                # make the use of extensions safe and manageable, there is a strict set of
                # governance applied to the definition and use of extensions. Though any
                # implementer can define an extension, there is a set of requirements that SHALL
                # be met as part of the definition of the extension. Applications processing a
                # resource are required to check for modifier extensions.
                #
                # Modifier extensions SHALL NOT change the meaning of any elements on Resource
                # or DomainResource (including cannot change the meaning of modifierExtension
                # itself).
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
                            extension_depth=extension_depth,
                            max_extension_depth=max_extension_depth,
                            include_modifierExtension=include_modifierExtension,
                            use_date_for=use_date_for,
                            parent_path=my_parent_path,
                        )
                    ),
                    True,
                ),
                # The definition of the search parameter that describes this part.
                StructField(
                    "definition",
                    canonicalSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                        include_modifierExtension=include_modifierExtension,
                        use_date_for=use_date_for,
                        parent_path=my_parent_path + ".definition",
                    ),
                    True,
                ),
                # A sub-expression that defines how to extract values for this component from
                # the output of the main SearchParameter.expression.
                StructField("expression", StringType(), True),
            ]
        )
        if not include_extension:
            schema.fields = [
                c
                if c.name != "extension"
                else StructField("extension", StringType(), True)
                for c in schema.fields
            ]

        if not include_modifierExtension:
            schema.fields = [
                c
                if c.name != "modifierExtension"
                else StructField("modifierExtension", StringType(), True)
                for c in schema.fields
            ]

        return schema
