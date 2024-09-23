Feature: Check Box Interaction On Opera PMS

    @checkboxClick
    Scenario: User check the button enable or not
        Given the user launches Opera application
        Then on Opera user clicks the toolbar button "Reservations"
        Then on Opera user clicks the toolbar button "Update"
        Then the user validates if button "New" is enabled
        Then the user validates if button "Check In" is disabled
        Then on Opera user clicks on text that contains "Close"
