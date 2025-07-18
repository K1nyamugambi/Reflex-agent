# Pyhop, version 1.2.2
## A simple HTN planning system written in Python

----

Copyright 2013 Dana S. Nau - <http://www.cs.umd.edu/~nau>

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at <http://www.apache.org/licenses/LICENSE-2.0>

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

----

Pyhop is a simple HTN planner written in Python. 
It works in both Python 2 and 3. 

Pyhop was easy to implement (less than 150 lines of code), and if you understand the basic ideas of HTN planning ([this presentation](http://www.cs.umd.edu/~nau/papers/nau2013game.pdf) contains a quick summary),
Pyhop should be easy to understand. For examples of how to use it, see the example files that come with it.

Pyhop's planning algorithm is like the one in [SHOP](http://www.cs.umd.edu/projects/shop/), but with several differences that should make it easier to integrate it with ordinary computer programs:

  - Pyhop represents states of the world using ordinary variable bindings, not logical propositions. A state is just a Python object that contains the variable bindings.  For example, you might write s.loc['v'] = 'd' to say that vehicle v is at location d in state s.
  
  - To write HTN operators and methods for Pyhop, you don't need to learn a specialized planning language. Instead, you write them as ordinary Python functions. The current state (e.g., s in the above example) is passed to them as an argument.

----

Update, June 4, 2021:

- Modified blocks_world_methods.py and blocks_world_methods2.py to include a bug fix contributed by Éric Jacopin.
- Added a new example to blocks_world_examples.py, and moved some of the other examples into a new file.

----

Update, August 7, 2021:

- [GTPyhop](https://github.com/dananau/GTPyhop), a successor to Pyhop, is now available on github. [A publication about GTPyhop](https://www.cs.umd.edu/~nau/papers/nau2021gtpyhop.pdf) appeared in the HPlan workshop at ICAPS-2021.