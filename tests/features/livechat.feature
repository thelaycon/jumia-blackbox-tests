Feature: User can chat on website

	Scenario: User chats with customer care
		Given user visits any part of Jumia site
		When user clicks on chat button
		Then a chat conversation opens
		And user sends message
