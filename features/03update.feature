Feature: Update pages

    Scenario Outline: Update "<page>"
        Given "<page>" edit page is visible to producent user
        When user updates "<page>" text field
        And clicks on "Save" button
        Then updated information should replace old information on "<page>" detail page

    Examples:
            | page          |
            | Organizations |
            | Use Cases     |
            | Tools         |
            | Methods       |
