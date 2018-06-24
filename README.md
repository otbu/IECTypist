**IECTypist**

What is it: _IECTypist_ is a utility for parsing/converting IEC 61131-3 DUT (Data Unit Type) definitions. This is quite
 a special use-case really, I doubt you will ever need it.

 The conversion is done in two phases:
* The first phase converts the original DUT-definition (1st-form) to a system-independent 2nd-form.
* The second phase converts the system-independent 2nd-form to system-dependent 3rd-form.

The system-independent 2nd-form is the JSON format (when exported, which by default it is not).

The 3rd-form is user-selectable from a built-in set of supported 3rd-forms:
* **LANG_C**: C language type represention (the default).

Whether or not a mapping can exist between the 2nd-form and any 3rd-form, depends on the actual
implementation dialect of the 1st-form. 

Supported 1st-form implementation dialects of DUT definitions:
* **DIALECT_TWINCAT**: Each individual input file/string is interpreted as a single Beckhoff TwinCAT
DUT-definition (XML-based). This relates specifically to *.TcDUT files. The only type-definition
currently supported for _DIALECT_TWINCAT_ is the liniear data-structure (STRUCT) type-definition.
TwinCAT version supported is 3.1.x.

Supported 2nd to 3rd form mappings:
* **TWINCAT_TO_C**: The default mapping for _DIALECT_TWINCAT_ 1st-form. It converts to _LANG_C_.   


2018 - License is MIT.




