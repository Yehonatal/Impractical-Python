<h1><strong>PROJECT #3: FINDING PALINGRAMS</strong></h1>

<h2>The Objective</h2>

<p>Use Python to search an English language dictionary for two­word
palingrams. Analyze and optimize the palingram code using the cProfile tool.</p>

<h3></h3>


<h2>The Strategy</h2>
<p>palingrams read the same forward and backward</p>

<h2>The Pseudocode</h2>

* Load digital dictionary as a list of words
* Start an empty list to hold palingrams
* For word in word list:
  * Get length of word
  * If length > 1:
    * Loop through the letters in the word:
      * If reversed word fragment at front of word is in word list and letters after form a palindromic sequence:
        * Append word and reversed word to palingram list
      * If reversed word fragment at end of word is in word list and letters before form a palindromic sequence:
        * Append reversed word and word to palingram list
* Sort palingram list alphabetically
* Print word­pair palingrams from palingram lis


### **Time** 
    To Get Program Runtime
    
        import time

        start_time = time.time()

        // Code for program

        end_time = time.time()
        print(f"Runtime for this program was {end_time - start_time} seconds.")