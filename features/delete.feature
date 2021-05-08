Feature: Add pages

    Scenario Outline: Delete "<page>"
        Given producent user is at "<page>" detail page
        When user clicks on "Actions" -> "Delete"
        And user confirms page deletion
        Then "<page>" should disapper from "<page>" list page

    Examples:
            | page          |
            | Organizations |
            | Use Cases     |
            | Tools         |
            | Methods       |
