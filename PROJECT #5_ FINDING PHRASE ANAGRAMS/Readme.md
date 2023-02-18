<h1><strong>PROJECT #5: FINDING PHRASE ANAGRAMS</strong></h1>

<h2>The Objective</h2>

<p>Write a Python program that lets a user interactively build an anagram
phrase from the letters in their name.
<h3></h3>


<h2>The Strategy</h2>
<p>The brute­force method is a common approach used in online anagram generators.
These algorithms take a name and return lots of random anagram phrases (generally,
100s to 10,000+). Most of the returned phrases are nonsense, and scrolling through
hundreds of these can be a chore.
An alternative approach is to acknowledge that humans are best at contextual issues
and write a program that helps the human work through the problem. The computer
can take the initial name and provide words that can be made from some (or all) the
letters in it; the user can then choose a word that “makes sense.” The program will then
recalculate the word choices from the remaining letters in the name, repeating the
process until every letter is used or the possible word c/p>

<h2>The Pseudocode</h2>

* Load a dictionary file
* Accept a name from user
* Set limit = length of name
* Start empty list to hold anagram phrase
* While length of phrase < limit:t:
  * Generate list of dictionary words that fit in name
  * Present words to user
  * Present remaining letters to user
  * Present current phrase to user
  * Ask user to input word or start over
  * If user input can be made from remaining letters
    * Accept choice of new word or words from user
    * Remove letters in choice from letters in name
    * Return choice and remaining letters in name
  * If choice is not a valid selection
    * Ask user for new choice or let user start over
  * Add choice to phrase and show to user
  * Generate new list of words and repeat process
* When phrase length equals limit value
  * Display final phrase
  * Ask user to start over or to exit

