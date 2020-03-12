Feature: Center Search
  Scenario: Search for a center based on Zip Code
    Given i have internet connectivity
      When we visit kindercare
      Then it should have a title "KinderCare | Child Daycare Centers & Early Education Programs"
      Then I click Find Your Center
      Then it should have taken me to "Center Search Results | KinderCare"
      Then i enter my zip code
      Then and click Search Again
      Then i can see the center and click Tuition and Openings
      Then i can see "Powell KinderCare"