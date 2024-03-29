Feature: Add pages

    Scenario Outline: Add "<page>"
        Given producent user clicks on "Add new" -> "<page>"
        When user enters required "<page>" information
        And clicks on "Save" button
        Then added "<page>" detail page is accessible

    Examples:
            | page          |
            | Organizations |
            | Use Cases     |
            | Tools         |
            | Methods       |
