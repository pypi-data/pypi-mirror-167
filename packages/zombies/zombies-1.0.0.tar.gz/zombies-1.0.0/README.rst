zombies
========
Run brainfuck code.


License
--------
MIT


Installation
-------------
.. code-block:: sh

    $ pip install zombies


Python Usage
-------------
.. code-block:: py

    import zombies

    interpreter = zombies.BF()
    code = '''
    >+++++++++[<++++++++>-]<.>+++++++[<++++>-]<+.+++++++..+++.[-]
    >++++++++[<++++>-] <.>+++++++++++[<++++++++>-]<-.--------.+++
    .------.--------.[-]>++++++++[<++++>- ]<+.[-]++++++++++.
    '''
    interpreter.run(code)  # Hello World!

    # you can also run a .bf file
    interpreter.run('helloworld.bf')


Command Line Usage
-------------------
Run a `.bf` file

.. code-block:: sh

    $ zombies helloworld.bf


Use the REPL

.. code-block:: sh

    $ zombies
    Brainfuck REPL made in Python | zombies 1.0.0a by The Master | License MIT
    Type "stop" to exit
    \\\ >>++<<+-


Code Formatting
----------------
All code should be formatted with `black`.
