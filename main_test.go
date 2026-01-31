package main_test

import (
	"fmt"
	"strings"
	"testing"
)

const (
	padding   = "foobarbaz"
	maxLength = 40
)

func BenchmarkCompare(b *testing.B) {
	expected := buildCompareString()
	base := strings.Repeat("0", maxLength)

	for i := range maxLength + 1 {
		actual := expected[:i] + base[i:]
		b.Run(fmt.Sprintf("matching=%d", i), func(b *testing.B) {
			for b.Loop() {
				_ = expected == actual
			}
		})
	}
}

func buildCompareString() string {
	return strings.Repeat(padding, maxLength/len(padding)) +
		padding[:maxLength%len(padding)]
}
