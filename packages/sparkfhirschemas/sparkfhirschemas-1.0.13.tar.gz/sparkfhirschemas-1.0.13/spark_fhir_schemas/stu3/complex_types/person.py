from typing import Union, List, Optional

from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    ArrayType,
    DateType,
    BooleanType,
    DataType,
)


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class PersonSchema:
    """
    Demographics and administrative information about a person independent of a
    specific health-related context.
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
        Demographics and administrative information about a person independent of a
        specific health-related context.


        id: The logical id of the resource, as used in the URL for the resource. Once
            assigned, this value never changes.

        extension: May be used to represent additional information that is not part of the basic
            definition of the resource. In order to make the use of extensions safe and
            manageable, there is a strict set of governance  applied to the definition and
            use of extensions. Though any implementer is allowed to define an extension,
            there is a set of requirements that SHALL be met as part of the definition of
            the extension.

        meta: The metadata about the resource. This is content that is maintained by the
            infrastructure. Changes to the content may not always be associated with
            version changes to the resource.

        implicitRules: A reference to a set of rules that were followed when the resource was
            constructed, and which must be understood when processing the content.

        language: The base language in which the resource is written.

        text: A human-readable narrative that contains a summary of the resource, and may be
            used to represent the content of the resource to a human. The narrative need
            not encode all the structured data, but is required to contain sufficient
            detail to make it "clinically safe" for a human to just read the narrative.
            Resource definitions may define what content should be represented in the
            narrative to ensure clinical safety.

        contained: These resources do not have an independent existence apart from the resource
            that contains them - they cannot be identified independently, and nor can they
            have their own independent transaction scope.

        resourceType: This is a Person resource

        identifier: Identifier for a person within a particular scope.

        name: A name associated with the person.

        telecom: A contact detail for the person, e.g. a telephone number or an email address.

        gender: Administrative Gender.

        birthDate: The birth date for the person.

        address: One or more addresses for the person.

        photo: An image that can be displayed as a thumbnail of the person to enhance the
            identification of the individual.

        managingOrganization: The organization that is the custodian of the person record.

        active: Whether this person's record is in active use.

        link: Link to a resource that concerns the same actual person.

        """
        from spark_fhir_schemas.stu3.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.stu3.complex_types.meta import MetaSchema
        from spark_fhir_schemas.stu3.complex_types.narrative import NarrativeSchema
        from spark_fhir_schemas.stu3.simple_types.resourcelist import ResourceListSchema
        from spark_fhir_schemas.stu3.complex_types.identifier import IdentifierSchema
        from spark_fhir_schemas.stu3.complex_types.humanname import HumanNameSchema
        from spark_fhir_schemas.stu3.complex_types.contactpoint import (
            ContactPointSchema,
        )
        from spark_fhir_schemas.stu3.complex_types.address import AddressSchema
        from spark_fhir_schemas.stu3.complex_types.attachment import AttachmentSchema
        from spark_fhir_schemas.stu3.complex_types.reference import ReferenceSchema
        from spark_fhir_schemas.stu3.complex_types.person_link import Person_LinkSchema

        if (
            max_recursion_limit and nesting_list.count("Person") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Person"]
        schema = StructType(
            [
                # The logical id of the resource, as used in the URL for the resource. Once
                # assigned, this value never changes.
                StructField("id", StringType(), True),
                # May be used to represent additional information that is not part of the basic
                # definition of the resource. In order to make the use of extensions safe and
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
                # The metadata about the resource. This is content that is maintained by the
                # infrastructure. Changes to the content may not always be associated with
                # version changes to the resource.
                StructField(
                    "meta",
                    MetaSchema.get_schema(
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
                # A reference to a set of rules that were followed when the resource was
                # constructed, and which must be understood when processing the content.
                StructField("implicitRules", StringType(), True),
                # The base language in which the resource is written.
                StructField("language", StringType(), True),
                # A human-readable narrative that contains a summary of the resource, and may be
                # used to represent the content of the resource to a human. The narrative need
                # not encode all the structured data, but is required to contain sufficient
                # detail to make it "clinically safe" for a human to just read the narrative.
                # Resource definitions may define what content should be represented in the
                # narrative to ensure clinical safety.
                StructField(
                    "text",
                    NarrativeSchema.get_schema(
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
                # These resources do not have an independent existence apart from the resource
                # that contains them - they cannot be identified independently, and nor can they
                # have their own independent transaction scope.
                StructField(
                    "contained",
                    ArrayType(
                        ResourceListSchema.get_schema(
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
                # This is a Person resource
                StructField("resourceType", StringType(), True),
                # Identifier for a person within a particular scope.
                StructField(
                    "identifier",
                    ArrayType(
                        IdentifierSchema.get_schema(
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
                # A name associated with the person.
                StructField(
                    "name",
                    ArrayType(
                        HumanNameSchema.get_schema(
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
                # A contact detail for the person, e.g. a telephone number or an email address.
                StructField(
                    "telecom",
                    ArrayType(
                        ContactPointSchema.get_schema(
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
                # Administrative Gender.
                StructField("gender", StringType(), True),
                # The birth date for the person.
                StructField("birthDate", DateType(), True),
                # One or more addresses for the person.
                StructField(
                    "address",
                    ArrayType(
                        AddressSchema.get_schema(
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
                # An image that can be displayed as a thumbnail of the person to enhance the
                # identification of the individual.
                StructField(
                    "photo",
                    AttachmentSchema.get_schema(
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
                # The organization that is the custodian of the person record.
                StructField(
                    "managingOrganization",
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
                # Whether this person's record is in active use.
                StructField("active", BooleanType(), True),
                # Link to a resource that concerns the same actual person.
                StructField(
                    "link",
                    ArrayType(
                        Person_LinkSchema.get_schema(
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
