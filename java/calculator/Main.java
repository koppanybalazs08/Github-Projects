/*Array, List, és JavaFX importok*/
import java.util.Arrays;
import java.util.List;
import javafx.application.Application;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.layout.GridPane;
import javafx.stage.Stage;

/*Main class*/
public class Main extends Application {

    @Override
    public void start(Stage stage) {
        String[] calculation = {""};

        /*Számítás és eredmény felirat létrehozása*/
        Label calcLabel = new Label(calculation[0]);
        Label resultLabel = new Label(" = ");

        /*Számok gombajinak létrehozása*/
        Button[] numbersBtn = new Button[10];
        for (int i = 0; i < 10; i++) {
            Button tempBtn = new Button("" + i);

            /*Gomb funkciók megadása*/
            tempBtn.setOnAction(e -> {
                calculation[0] += tempBtn.getText();
                calcLabel.setText(calculation[0]);
            });

            numbersBtn[i] = tempBtn;
        }

        /*Műveleti jelek gombjainak létrehozása*/

        /*Összeadás*/
        Button addBtn = new Button("+");
        addBtn.setOnAction(e -> {
            calculation[0] += "+";
            calcLabel.setText(calculation[0]);
        });

        /*Kivonás*/
        Button subtractBtn = new Button("-");
        subtractBtn.setOnAction(e -> {
            calculation[0] += "-";
            calcLabel.setText(calculation[0]);
        });

        /*Szorzás*/
        Button multiplyBtn = new Button("x");
        multiplyBtn.setOnAction(e -> {
            calculation[0] += "*";
            calcLabel.setText(calculation[0]);
        });

        /*Osztás*/
        Button divideBtn = new Button("/");
        divideBtn.setOnAction(e -> {
            calculation[0] += "/";
            calcLabel.setText(calculation[0]);
        });

        /*"Kiszámolás" / "=" gomb létrehozása*/
        Button calcBtn = new Button("=");
        calcBtn.setOnAction(e -> {
            try{
                resultLabel.setText(" = " + Calculate(calculation[0]));
            }
            catch(java.lang.NumberFormatException exception){
                resultLabel.setText(" = ERROR");
            }
            calculation[0] = "";
            calcLabel.setText(calculation[0]);
        });

        /*Elemek elhelyezése egy GridPane()-ben*/
        GridPane grid = new GridPane();
        grid.setHgap(10);
        grid.setVgap(10);
        grid.setAlignment(Pos.CENTER);

        grid.add(calcLabel, 0, 0);
        GridPane.setColumnSpan(calcLabel, 3);
        grid.add(resultLabel, 3, 0); //col 3, row 0

        grid.add(numbersBtn[1],0,1);
        grid.add(numbersBtn[2],1,1);
        grid.add(numbersBtn[3],2,1);
        grid.add(addBtn, 3, 1);

        grid.add(numbersBtn[4],0,2);
        grid.add(numbersBtn[5],1,2);
        grid.add(numbersBtn[6],2,2);
        grid.add(subtractBtn, 3, 2);

        grid.add(numbersBtn[7],0,3);
        grid.add(numbersBtn[8],1,3);
        grid.add(numbersBtn[9],2,3);
        grid.add(multiplyBtn, 3, 3);

        grid.add(numbersBtn[0],1,4);
        grid.add(divideBtn, 3, 4);
        grid.add(calcBtn, 2, 4);

        /*Scene beállítása*/
        Scene scene = new Scene(grid, 300, 200);

        stage.setTitle("Calculator");
        stage.setScene(scene);
        stage.show();
    }

    public double Calculate(String calculation) {
        String num1 = "";
        String operand = "";
        String num2 = "";
        double result;
        List<String> validNums = Arrays.asList("0", "1", "2", "3", "4", "5", "6", "7", "8", "9");

        /*A két szám keresése a "calculation" str-ben*/
        for (int i = 0; i < calculation.length(); i++) {

            String nextChar = Character.toString((calculation.charAt(i)));
            if (operand.isEmpty() && validNums.contains(nextChar)) {
                num1 += nextChar;
            } else if (operand.length() == 1 && validNums.contains(nextChar)) {
                num2 += nextChar;
            } else {
                operand += nextChar;
            }
        }

        /*Műveleti jel keresése*/
        operand = Character.toString((operand.charAt(0)));

        /*Eredmény kiszámítása switch-el*/
        result = switch (operand) {
            case "+" ->
                Double.parseDouble(num1) + Double.parseDouble(num2);
            case "-" ->
                Double.parseDouble(num1) - Double.parseDouble(num2);
            case "*" ->
                Double.parseDouble(num1) * Double.parseDouble(num2);
            case "/" ->
                Double.parseDouble(num1) / Double.parseDouble(num2);
            default ->
                0;
        };
        return result;
    }

    public static void main(String[] args) {
        launch();
    }
}
