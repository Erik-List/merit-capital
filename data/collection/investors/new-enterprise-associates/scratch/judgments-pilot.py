import judge_lib as jl
L = [jl.cls("42floors", status="acquired", rng="below_1b", city="San Francisco", focus="Consumer & Marketplaces",
            note="Acquired by Knotel in 2019; the firm's own exit line and the a16z book agree.")]
jl.write("pilot", L)
