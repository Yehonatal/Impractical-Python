<h1><strong>PROJECT #4: FINDING SINGLE-WORD ANAGRAMS</strong></h1>

<h2>The Objective</h2>

<p>Use Python and a dictionary file to find all the single­word anagrams for a
given English word or single name.
<h3></h3>


<h2>The Strategy</h2>
<p>More than 600 newspapers and 100 internet sites carry an anagram game called
Jumble. Created in 1954, it’s now the most recognized word­scramble game in the
world. Jumble can be really frustrating, but finding anagrams is almost as easy as
finding palindromes—you just need to know the common characteristic of all
anagrams: they must have the same number of the same letters.</p>

<h2>The Pseudocode</h2>

* Load digital dictionary as a list of words
* Accept a word from user
* Start an empty list to hold anagrams
* Loop through each word in the word list:
  * Sort the word
  * if word sorted is equal to user­word sorted::
    * Append word to anagrams list:
* Print anagrams list
