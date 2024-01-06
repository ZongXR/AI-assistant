/**
 * 修改文字
 * @param timeout
 */
const changeHeaderText = function (timeout) {
    if ($("#video_header").text() === "远程监控"){
        $("#video_header").text(timeout.toString() + "秒后服务器关闭");
    }else{
        let header = $("#video_header").text();
        let seconds = parseInt(header.match("^-?\\d+")[0]);
        if (seconds - 1 < 0)
            window.clearInterval(shutdownIntervalId);
        else
            $("#video_header").text((seconds - 1).toString() + "秒后服务器关闭");
    }
}

/**
 * 关闭当前标签页
 */
const closeWindow = function(){
    window.opener = null;
    window.open('','_self');
    window.close();
}

/**
 * 关机
 */
function shutdown(dom) {
    let url, data;
    if ($("#btn_shutdown").text() === "关机") {
        url = "/shutdown";
        data = JSON.stringify({"minutes": 0});
    } else {
        url = "/cancel_shutdown";
        data = JSON.stringify({});
    }
    $.ajax({
        type: "POST",
        contentType: "application/json;charset=utf-8",
        dataType: "json",
        url: url,
        data: data,
        success: function (response) {
            if ($("#btn_shutdown").text() === "关机") {
                if (response.data >= 0) {
                    shutdownIntervalId = window.setInterval(changeHeaderText, 1000, response.data * 1000);
                    shutdownTimeoutId = window.setTimeout(closeWindow, response.data * 1000);
                    $("#btn_shutdown").text("取消关机");
                } else {
                    console.log(response.data);
                    window.alert("执行关机失败，请手动关机");
                }
            } else {
                if (response.data >= 0) {
                    window.clearInterval(shutdownIntervalId);
                    window.clearTimeout(shutdownTimeoutId);
                    $("#video_header").text("远程监控");
                    $("#btn_shutdown").text("关机");
                } else {
                    console.log(response.data);
                    window.alert("取消关机失败，请手动取消");
                }
            }
        },
        error: function (jqXHR, textStatus, errorThrown) {}
    });
}