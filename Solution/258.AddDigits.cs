static public int Add(int x, int y) {//=B5=DD=B9=E9
	return y == 0 ? x : Add(x ^ y, (x &amp; y) << 1);
}

static public int Add(int x, int y) {//=B5=DD=B9=E9
	if (y == 0) {
		return x;
	}
	int sum = x ^ y;
	int carry = (x &amp; y) << 1;
	return Add(sum, carry);
}

static public int Add(int x, int y) {//=D1=AD=BB=B7
	int sum = 0;
	while (y != 0) {
		sum = x ^ y;
		y = (x &amp; y) << 1;
		x = sum;
	}
	return sum;
}
