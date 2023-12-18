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

/**
 * 设置摄像头的 暂停/开始 按钮
 */
const setButtonCameraText = function(){
    $.ajax({
        type: "POST",
        contentType: "application/json;charset=utf-8",
        dataType: "json",
        data: JSON.stringify({}),
        url: "/is_server_camera_enabled",
        success: function (response) {
            if (response.data) {
                $("#btn_camera").text("暂停");
            } else {
                $("#btn_camera").text("开始");
            }
        },
        error: function (jqXHR, textStatus, errorThrown) {}
    });
}