/*
FONTOS GO PARANCSOK
go run main.go
go mod init main
go mod tidy
go build main.go
*/

package main

/*importok*/
import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	/*array*/
	muveletArray := [4]string{"+", "-", "*", "/"}

	input := getInput()

	/*Main loop*/
	for input != "exit" {
		muveletHely := -1
		muveletHasznalt := ""

		/*műveleti jel keresése*/
		for _, muvelet := range muveletArray {
			if muveletHely == -1 {
				muveletHely = strings.Index(input, muvelet)
				muveletHasznalt = muvelet
			}
		}

		/*számok keresése*/
		szam1, _ := strconv.ParseFloat(strings.TrimSpace(input[0:muveletHely]), 3)
		szam2, _ := strconv.ParseFloat(strings.TrimSpace(input[muveletHely+1:]), 3)

		/*művelet végrehajtása switch-el*/
		var eredmeny float64
		switch muveletHasznalt {
		case "+":
			eredmeny = szam1 + szam2
		case "-":
			eredmeny = szam1 - szam2
		case "*":
			eredmeny = szam1 * szam2
		case "/":
			eredmeny = szam1 / szam2
		}

		fmt.Println(eredmeny)
		input = getInput()
	}

}

func getInput() string {
	var input string
	/*Scanner létrehozása*/
	sc := bufio.NewScanner(os.Stdin)

	/*Scannelés (input szerzés billentyűzetről)*/
	fmt.Print("Adj meg egy számolás (max 1 művelet, exit a kilépéshez): ")
	sc.Scan()
	input = sc.Text()

	return input

}
