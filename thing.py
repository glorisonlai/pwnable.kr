import os

files = [
    "fd",
    "collision",
    "bof",
    "flag",
    "passcode",
    "random",
    "input",
    "leg",
    "mistake",
    "shellshock",
    "coin1",
    "blackjack",
    "lotto",
    "cmd1",
    "cmd2",
    "uaf",
    "memcpy",
    "asm",
    "unlink",
    "blukat",
    "horcruxes",
    "brain fuck",
    "md5 calculator",
    "simple login",
    "otp",
    "ascii_easy",
    "tiny_easy",
    "fsb",
    "dragon",
    "fix",
    "syscall",
    "crypto1",
    "echo1",
    "echo2",
    "rsa calculator",
    "note",
    "alloca",
    "loveletter",
    "rootkit",
    "dos4fun",
    "ascii",
    "aeg",
    "coin2",
    "maze",
    "wtf",
    "sudoku",
    "starcraft",
    "cmd3",
    "elf",
    "lfh",
    "lokihardt",
    "asg",
    "hunter",
    "mipstake",
    "unexploitable",
    "tiny",
    "softmmu",
    "towelroot",
    "nuclear",
    "malware",
    "exploitable",
    "tiny_hard",
    "kcrc",
    "exynos",
    "combabo calculator",
    "pwnsandbox",
    "crcgen"
]

for thing in files:
	try:
		os.mkdir(thing)
	except:
		pass
