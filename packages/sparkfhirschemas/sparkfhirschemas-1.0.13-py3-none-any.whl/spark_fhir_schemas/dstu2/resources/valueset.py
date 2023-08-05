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
class ValueSetSchema:
    """
    A value set specifies a set of codes drawn from one or more code systems.
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
        A value set specifies a set of codes drawn from one or more code systems.
        If the element is present, it must have either a @value, an @id, or extensions


            id: The logical id of the resource, as used in the URL for the resource. Once
        assigned, this value never changes.
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
            extension: May be used to represent additional information that is not part of the basic
        definition of the resource. In order to make the use of extensions safe and
        manageable, there is a strict set of governance  applied to the definition and
        use of extensions. Though any implementer is allowed to define an extension,
        there is a set of requirements that SHALL be met as part of the definition of
        the extension.
            modifierExtension: May be used to represent additional information that is not part of the basic
        definition of the resource, and that modifies the understanding of the element
        that contains it. Usually modifier elements provide negation or qualification.
        In order to make the use of extensions safe and manageable, there is a strict
        set of governance applied to the definition and use of extensions. Though any
        implementer is allowed to define an extension, there is a set of requirements
        that SHALL be met as part of the definition of the extension. Applications
        processing a resource are required to check for modifier extensions.
            url: An absolute URL that is used to identify this value set when it is referenced
        in a specification, model, design or an instance. This SHALL be a URL, SHOULD
        be globally unique, and SHOULD be an address at which this value set is (or
        will be) published.
            identifier: Formal identifier that is used to identify this value set when it is
        represented in other formats, or referenced in a specification, model, design
        or an instance.
            version: Used to identify this version of the value set when it is referenced in a
        specification, model, design or instance. This is an arbitrary value managed
        by the profile author manually and the value should be a timestamp.
            name: A free text natural language name describing the value set.
            status: The status of the value set.
            experimental: This valueset was authored for testing purposes (or
        education/evaluation/marketing), and is not intended to be used for genuine
        usage.
            publisher: The name of the individual or organization that published the value set.
            contact: Contacts to assist a user in finding and communicating with the publisher.
            date: The date that the value set status was last changed. The date must change when
        the business version changes, if it does, and it must change if the status
        code changes. In addition, it should change when the substantive content of
        the implementation guide changes (e.g. the 'content logical definition').
            lockedDate: If a locked date is defined, then the Content Logical Definition must be
        evaluated using the current version of all referenced code system(s) and value
        set instances as of the locked date.
            description: A free text natural language description of the use of the value set - reason
        for definition, "the semantic space" to be included in the value set,
        conditions of use, etc. The description may include a list of expected usages
        for the value set and can also describe the approach taken to build the value
        set.
            useContext: The content was developed with a focus and intent of supporting the contexts
        that are listed. These terms may be used to assist with indexing and searching
        of value set definitions.
            immutable: If this is set to 'true', then no new versions of the content logical
        definition can be created.  Note: Other metadata might still change.
            requirements: Explains why this value set is needed and why it has been constrained as it
        has.
            copyright: A copyright statement relating to the value set and/or its contents. Copyright
        statements are generally legal restrictions on the use and publishing of the
        value set.
            extensible: Whether this is intended to be used with an extensible binding or not.
            codeSystem: A definition of a code system, inlined into the value set (as a packaging
        convenience). Note that the inline code system may be used from other value
        sets by referring to its (codeSystem.system) directly.
            compose: A set of criteria that provide the content logical definition of the value set
        by including or excluding codes from outside this value set.
            expansion: A value set can also be "expanded", where the value set is turned into a
        simple collection of enumerated codes. This element holds the expansion, if it
        has been performed.
        """
        # id
        from spark_fhir_schemas.dstu2.simple_types.id import idSchema

        # meta
        from spark_fhir_schemas.dstu2.complex_types.meta import MetaSchema

        # implicitRules
        from spark_fhir_schemas.dstu2.simple_types.uri import uriSchema

        # language
        # type = code
        # text
        from spark_fhir_schemas.dstu2.complex_types.narrative import NarrativeSchema

        # contained
        from spark_fhir_schemas.dstu2.complex_types.resourcecontainer import (
            ResourceContainerSchema,
        )

        # extension
        from spark_fhir_schemas.dstu2.complex_types.extension import ExtensionSchema

        # identifier
        from spark_fhir_schemas.dstu2.complex_types.identifier import IdentifierSchema

        # contact
        from spark_fhir_schemas.dstu2.backbone_elements.valuesetcontact import (
            ValueSetContactSchema,
        )

        # date
        from spark_fhir_schemas.dstu2.simple_types.datetime import dateTimeSchema

        # useContext
        from spark_fhir_schemas.dstu2.complex_types.codeableconcept import (
            CodeableConceptSchema,
        )

        # codeSystem
        from spark_fhir_schemas.dstu2.backbone_elements.valuesetcodesystem import (
            ValueSetCodeSystemSchema,
        )

        # compose
        from spark_fhir_schemas.dstu2.backbone_elements.valuesetcompose import (
            ValueSetComposeSchema,
        )

        # expansion
        from spark_fhir_schemas.dstu2.backbone_elements.valuesetexpansion import (
            ValueSetExpansionSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("ValueSet") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["ValueSet"]
        schema = StructType(
            [
                # The logical id of the resource, as used in the URL for the resource. Once
                # assigned, this value never changes.
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
                StructField(
                    "implicitRules",
                    uriSchema.get_schema(
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
                        ResourceContainerSchema.get_schema(
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
                            extension_depth=extension_depth + 1,
                            max_extension_depth=max_extension_depth,
                        )
                    ),
                    True,
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the resource, and that modifies the understanding of the element
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
                # An absolute URL that is used to identify this value set when it is referenced
                # in a specification, model, design or an instance. This SHALL be a URL, SHOULD
                # be globally unique, and SHOULD be an address at which this value set is (or
                # will be) published.
                StructField(
                    "url",
                    uriSchema.get_schema(
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
                # Formal identifier that is used to identify this value set when it is
                # represented in other formats, or referenced in a specification, model, design
                # or an instance.
                StructField(
                    "identifier",
                    IdentifierSchema.get_schema(
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
                # Used to identify this version of the value set when it is referenced in a
                # specification, model, design or instance. This is an arbitrary value managed
                # by the profile author manually and the value should be a timestamp.
                StructField("version", StringType(), True),
                # A free text natural language name describing the value set.
                StructField("name", StringType(), True),
                # The status of the value set.
                StructField("status", StringType(), True),
                # This valueset was authored for testing purposes (or
                # education/evaluation/marketing), and is not intended to be used for genuine
                # usage.
                StructField("experimental", BooleanType(), True),
                # The name of the individual or organization that published the value set.
                StructField("publisher", StringType(), True),
                # Contacts to assist a user in finding and communicating with the publisher.
                StructField(
                    "contact",
                    ArrayType(
                        ValueSetContactSchema.get_schema(
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
                # The date that the value set status was last changed. The date must change when
                # the business version changes, if it does, and it must change if the status
                # code changes. In addition, it should change when the substantive content of
                # the implementation guide changes (e.g. the 'content logical definition').
                StructField(
                    "date",
                    dateTimeSchema.get_schema(
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
                # If a locked date is defined, then the Content Logical Definition must be
                # evaluated using the current version of all referenced code system(s) and value
                # set instances as of the locked date.
                StructField("lockedDate", DateType(), True),
                # A free text natural language description of the use of the value set - reason
                # for definition, "the semantic space" to be included in the value set,
                # conditions of use, etc. The description may include a list of expected usages
                # for the value set and can also describe the approach taken to build the value
                # set.
                StructField("description", StringType(), True),
                # The content was developed with a focus and intent of supporting the contexts
                # that are listed. These terms may be used to assist with indexing and searching
                # of value set definitions.
                StructField(
                    "useContext",
                    ArrayType(
                        CodeableConceptSchema.get_schema(
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
                # If this is set to 'true', then no new versions of the content logical
                # definition can be created.  Note: Other metadata might still change.
                StructField("immutable", BooleanType(), True),
                # Explains why this value set is needed and why it has been constrained as it
                # has.
                StructField("requirements", StringType(), True),
                # A copyright statement relating to the value set and/or its contents. Copyright
                # statements are generally legal restrictions on the use and publishing of the
                # value set.
                StructField("copyright", StringType(), True),
                # Whether this is intended to be used with an extensible binding or not.
                StructField("extensible", BooleanType(), True),
                # A definition of a code system, inlined into the value set (as a packaging
                # convenience). Note that the inline code system may be used from other value
                # sets by referring to its (codeSystem.system) directly.
                StructField(
                    "codeSystem",
                    ValueSetCodeSystemSchema.get_schema(
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
                # A set of criteria that provide the content logical definition of the value set
                # by including or excluding codes from outside this value set.
                StructField(
                    "compose",
                    ValueSetComposeSchema.get_schema(
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
                # A value set can also be "expanded", where the value set is turned into a
                # simple collection of enumerated codes. This element holds the expansion, if it
                # has been performed.
                StructField(
                    "expansion",
                    ValueSetExpansionSchema.get_schema(
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
