from Supplement import UInput

user_prompts = ["\n What will be the Processor of your new PC? \n (A) Intel i9 5th GEN 3.1 GHZ \n (B) AMD Ryzen 3.5 "
                "GHZ \n (C) Snapdragon A11 \n ",
                "\n What will be the RAM size? \n (A) 4GB \n (B) 8GB \n (C) 16GB \n ",
                "\n What will be the SDD size? \n (A) 256GB \n (B) 512GB \n (C) 1TB \n ",
                "\n What will be the OS? \n (A) MAC OS \n (B) Windows \n (C) Linux \n ",
                "\n What will be the GPU? \n (A) Nvidia GPU \n (B) AMD GPU  \n (C) Intel Integrated Graphics \n "
                ]

PC_Structure = [
    UInput(user_prompts[0], 1000, 900, 600),
    UInput(user_prompts[1], 30, 100, 250),
    UInput(user_prompts[2], 200, 400, 700),
    UInput(user_prompts[3], 200, 100, 3),
    UInput(user_prompts[4], 900, 500, 250),
    UInput("\n What is its Case Build? \n (A) RBG Lights \n (B) Plain Build \n (C) See-Through Case \n ", 300, 50, 100),
]


def PC_Builder(build):
    value = 0
    validity = 0
    for i in build:
        answer = input(i.prompt)
        if answer.lower() == "a":
            value += i.p1
        elif answer.lower() == "b":
            value += i.p2
        elif answer.lower() == "c":
            value += i.p3
        else:
            validity += 1
    if validity == len(build):
        print("All of your Inputs were Invalid.")
    elif 1 <= validity < len(build):
        print("Some of your Inputs were Invalid.")
    else:
        print("\n Congratulations Your PC is Complete. It will Cost $", value, ".")


PC_Builder(PC_Structure)
