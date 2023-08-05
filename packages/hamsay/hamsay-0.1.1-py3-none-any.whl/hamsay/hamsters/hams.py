"""The Magic!"""
from textwrap import dedent


def balloon_message(msg):
    """
    What they say

    Parameters:
        msg (String): The message that goes into the balloon.

    Returns:
        output: A comic balloon with a stupid message.
    """

    phrase = " ".join(msg)
    topbar = "-" * len(phrase)
    bottombar = "-" * len(phrase)
    output = dedent(
        f"""
     .{topbar}.
    ( {phrase} )
     '{bottombar}'
         \\
	"""
    )
    return output


def hamster(msg):
    """
    The fat one.

    Parameters:
        msg (String): The message that this guy says.

    """
    ham_msg = (
        balloon_message(msg)
        + r"""        _           _
      (`-`;-'```'-;`-`)
       \.'         './
       |             |
       ;   0     0   ;
       | =         = |
     ; \   '._Y_.'   / ;
    ;   `-._ \|/ _.-'   ;
   ;        `'''`        ;
   ;    `''-.   .-''`    ;
  ( ;  '--._ \ / _.--   ; )
  :  `.   `/|| ||\`   .'  :
   '.  '-._       _.-'   .'
   (((-'`  `'''''`   `'-)))

    """
    )
    print(ham_msg)


def pervert(msg):
    """
    Nice one.

    Parameters:
        msg (String): The message that this guy says.

    """
    ham_msg = (
        balloon_message(msg)
        + r"""            o_
         .-"  ".          
       ."    _-'-""--o        
      J    ,"" _      ".
   .-",___,)____)___),-'
    """
    )
    print(ham_msg)


if __name__ == "__main__":
    print(balloon_message("like a comic!"))
    hamster("lovely")
    pervert("what a pervert")
