# roach.py
# Fully self-reversible "inside-out" payload demo

def invert_bits(data: bytes) -> bytes:
	"""Bitwise invert (flip 0<->1)"""
	return bytes(b ^ 0xFF for b in data)

def inside_out(text: str) -> str:
	"""Perfectly reversible inside-out transformation"""
	# Use full reversal (mirror) instead of half swap
	return text[::-1]

def logic_flip(x: bool) -> bool:
	"""Logical inversion that yields same output"""
	return not(not(x))

def main():
	payload = b"racecar"
	inverted = invert_bits(payload)
	reinverted = invert_bits(inverted)
	assert reinverted == payload  # bitwise symmetry

	text = payload.decode()
	flipped_text = inside_out(text)
	unflipped_text = inside_out(flipped_text)
	assert unflipped_text == text  # structural symmetry

	logic_result = logic_flip(True)
	print("Logic result:", logic_result)
	print("Inside-out reversible text:", flipped_text)
	print("Bit inversion reversible:", reinverted.decode(errors='ignore'))

if __name__ == "__main__":
	main()
