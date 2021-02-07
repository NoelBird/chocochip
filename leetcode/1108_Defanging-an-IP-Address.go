func defangIPaddr(address string) string {
	rslt := []rune("")
	for i := 0; i < len(address); i++ {
		if address[i] == '.' {
			rslt = append(rslt, '[', '.', ']')
		} else {
			rslt = append(rslt, rune(address[i]))
		}
	}
	return string(rslt)
}