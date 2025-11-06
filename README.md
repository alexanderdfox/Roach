# 🪳 Roach — A Reversible "Inside-Out" Program

**Roach** is a conceptual Python demo that explores **reversibility, symmetry, and structural mirroring** in both logic and data.  
Like its namesake, it’s built to survive its own inversion — flip it, mirror it, or invert every bit, and it still crawls back to the same logical form.

---

## 🧠 Concept

`roach.py` is designed around the idea of **perfect reversibility**.  
It performs three layers of symmetry:

1. **Bitwise Inversion** — every byte in the payload is flipped (`0 ↔ 1`) and then restored.  
2. **Structural Inside-Out Flip** — the text payload is split in half and reversed (`AB → BA`).  
3. **Logical Reflection** — boolean logic is inverted twice (`not(not(x))`) to return to its original state.

All transformations are **self-canceling**.  
When applied twice, the program returns exactly to its initial state — a software palindrome.

---

## ⚙️ Usage

```bash
python3 roach.py
```

Expected output:

```
Logic result: True
Inside-out reversible text: loadInsideOutPay
Bit inversion reversible: InsideOutPayload
```

*(The inside-out text will differ depending on payload length.)*

---

## 🧩 Palindromic Payload Requirement

For **perfect reversibility**, the `payload` must itself be **palindromic** — meaning it reads the same forwards and backwards **after both structural and byte inversions**.

Example of valid payloads:

```python
payload = b"ABCCBA"
payload = b"madam"
payload = b"racecar"
```

If the payload is not palindromic, the internal symmetry will still perform correctly,  
but the **inside-out text check** may fail the assertion.

---

## 🔄 ASCII Diagram — Inside-Out Flip

```
Original Payload:     [ A  B  C  D  E  F ]
                          ↓      ↓
Inside-Out Operation: [ D  E  F | A  B  C ]
                          ↑      ↑
Reapply Flip → Back:  [ A  B  C  D  E  F ]
```

---

## 🔬 Symbolism

- **Roach** survives inversion — it’s an allegory for resilient code.  
- **Bit flips** mimic radiation or noise.  
- **Inside-out logic** echoes reversible computation, a concept in quantum and entropy-neutral systems.

---

## 🧩 Future Extensions

- Palindromic binary executables  
- Self-inverting machine code payloads  
- Entropy-balanced reversible OS kernels  

---

**Author:** Alexander Fox  
**License:** MIT  
**Tagline:** _“Flip it, invert it, and it still crawls back to life.”_ 🪳
