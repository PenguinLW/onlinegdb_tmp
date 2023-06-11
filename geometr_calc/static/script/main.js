$(function () {
    s_view($('h1').html("<select><option>-</option></option></select>"));
    //$('#paint').hide();
});
function s_view(self) {
    $('#paint').css('visibility', 'visible');
    let figure = ($(self).find('select option:selected')).html();

    // выбор элемента в селекте, при нажатии на который вызывать соответствующий конструктор класса
    $.ajax({
        type: "GET",
        url: "/show_store",
        success: function (response) {
            change_figure(
                (figure.toString()).replaceAll("\n", "").replaceAll(" ", ""),
                response
            );
        }
    });
    function change_figure(figure, response) {
        $('h1').text(figure);
        // console.log(figure.length, figure, figure == "круг", figure == "круг", figure === "круг");
        switch (figure) {
            case 'круг':
                figure = "p1";
                break;
            case 'квадрат':
                figure = "p2";
                break;
            case 'прямоугольник':
                figure = "p3";
                break;
            case 'треугольник':
                figure = "p4";
                break;
            case 'трапеция':
                figure = "p5";
                break;
            case 'ромб':
                figure = "p6";
                break;
            case 'сфера':
                figure = "v1";
                break;
            case 'куб':
                figure = "v2";
                break;
            case 'параллелепипед':
                figure = "v3";
                break;
            case 'пирамида':
                figure = "v4";
                break;
            case 'цилиндр':
                figure = "v5";
                break;
            case 'конус':
                figure = "v6";
                break;
            default:
                $('h1').text("random");
        }
        $("#paint img").attr(
            "src",
            "/"+figure+"/plot.png"
        );
        // for(resp in response) {
        //     for(el in response[resp]) {
        //
        //     }
        // }
    }
}