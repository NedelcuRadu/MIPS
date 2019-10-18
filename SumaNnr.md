```assembly
.data
x: .space 4
afis: .asciiz "Suma este "

.text

  main:
  
#Citeste X in $t0
li $v0,5
syscall
move $t0,$v0
sw $t0, x

li $t2,0 #i=0

  #Suma in $t1
loop: bge $t2,$t0,exit # if (i>=x): exit
      add $t1,$t2,$t1
      addi $t2,$t2,1
      j loop

  #Afisare text
exit: la $a0,afis
li $v0,4
syscall


  #Afisare suma
move $a0,$t1
li $v0,1
syscall

  #Return 0
li $v0,10
syscall
```
