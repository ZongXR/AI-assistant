/**
 * 暂停、开始捕获画面
 */
function enableServerCamera(dom) {
    $.ajax({
        type: "POST",
        contentType: "application/json;charset=utf-8",
        dataType: "json",
        url: "/enable_server_camera",
        data: JSON.stringify({"enable": $(dom).text() === "开始"}),
        success: function (response) {
            if (response.data) {
                $(dom).text("开始");
            } else {
                $(dom).text("暂停");
                window.location.reload("#server_camera");
            }
        },
        error: function (jqXHR, textStatus, errorThrown) {}
    });
}