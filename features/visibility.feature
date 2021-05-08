Feature: Hide/show pages

    Scenario Outline: Hide "<page>"
        Given producent user is at "<page>" detail page
        And "<page>" state is "Published"
        When user clicks on "State" -> "Retract"
        Then "<page>" should disapper from "<page>" list page for consument user

        Examples:
            | page          |
            | Organizations |
            | Use Cases     |
            | Tools         |
            | Methods       |


    Scenario Outline: Show "<page>"
        Given producent user is at "<page>" detail page
        And "<page>" state is "Private"
        When user clicks on "State" -> "Publish"
        Then "<page>" should disapper from "<page>" list page for consument user

        Examples:
            | page          |
            | Organizations |
            | Use Cases     |
            | Tools         |
            | Methods       |
