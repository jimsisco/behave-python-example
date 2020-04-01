Feature: Center Search
  Scenario: Search for a center based on Zip Code
    Given I have internet connectivity
      When we visit kindercare
      Then it should have a title "KinderCare | Child Daycare Centers & Early Education Programs"
      Then I click Find Your Center
      Then it should have taken me to "Center Search Results | KinderCare"
      Then I enter my zip code
      Then and click Search Again
      Then I can see the center and click Tuition and Openings
      Then I can see "Center Search Results | KinderCare"
      Then I enter First Name
      Then I enter Last Name
      Then I enter Email Address
      Then I Confirm Email Address