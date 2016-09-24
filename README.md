# nim-games
Implementation of differents nim games and resolver.

# Presentation of the games
## Chomp
This game is an implementation of the chomp game revisited.<br/>
The rules are very simple, you have a chocolate bar and you choose a square of this bar and you remove either the column or the row of this square.<br/>
The winner is the latest player who can play (ie the latest player who can remove a row or a column)
This game has not a real method to calculate the winning move but we surmised a solution for this.<br/>
If you can prove it, you can mail us with your proof at <wampixel@gmail.com>.

##Hackendot
This game is an implementation of the Von Neumman Hackendot resolved in 1979 by J. Ulehla.<br/>
This game use a forest of *n-trees* (each node of the tree have *n* childs max) and the goal of the game is to be the latest player to remove a node of the forest.<br/>
When you remove a node, you first choose a tree, then you choose a node and finally, you remove all the nodes of the path from the root to the selected node.<br/>
the method to calculate the winning move for this game has been demonstrated by J. Ulehla in it's <a href="http://download.springer.com/static/pdf/814/art%253A10.1007%252FBF01769768.pdf?originUrl=http%3A%2F%2Flink.springer.com%2Farticle%2F10.1007%2FBF01769768&token2=exp=1474704423~acl=%2Fstatic%2Fpdf%2F814%2Fart%25253A10.1007%25252FBF01769768.pdf%3ForiginUrl%3Dhttp%253A%252F%252Flink.springer.com%252Farticle%252F10.1007%252FBF01769768*~hmac=db493dae8659f5a0d399a174eff3a07b12a9da79fa643a94bc8842e1a86d1c3f">paper</a> in 1979.

##Simple Nim game
This game is the pile of match game.<br/>
This game use a set of matches. the winner of the game is the latest player who can remove a matches.<br/>
To remove a matches, choose a heap, take many match you want in this heap(you can remove 1 match to the complete heap).<br/>
this game use the <a href="http://www.archim.org.uk/eureka/27/games.html">Sprague-Grundy theorem</a> to calculate the winning move.<br/>

#Installation
Download and copy the repo in your favourite folder.

#Usage
Go to the python_sources folder and choose the folder of the game that you want to play.<br/>
To execute the games use :
* *./nim.py* for the simple nim game
* *./hackendot.py* for the hackendot game
* *./chomp.py* for the chomp game

#improvement
* we must use the rule *The latest player who can remove lost the game*
* add a GUI for all the games
