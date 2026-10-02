We know the flag is of the form BYTE{...}
So after base64 gave me BAIN{...} I checked for vignere and beaufort cipher and found the key using a simple c program
The vignere key was just random letters and even decoding gave nothing however the beaufort key was CYBR which would mean cyber so i got a hint that i was on the right path.
After beaufort decoding i got BYTE{bY73_L8A_ChuKA_B4dLaV} which clearly looks like "byte laa chuka badlav"
I ran it on leetspeak anyway and got BYTE{bYte_LbA_ChuKA_BadLaV}
