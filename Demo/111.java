package com.rbq.common.constant;

import com.rbq.common.constant.third.LunduEnum;

/**
 * @desc: APP常量枚举定义
 * @author: Cassius
 * @date: 2020-10-26
 */
public enum CodeEnum {
    /**
     * 订单状态
     */
    APPLY_STATUS_0("0","初始化"),
    APPLY_STATUS_1("1","审批中"),
    APPLY_STATUS_2("2","审批拒绝"),
    APPLY_STATUS_3("3","审批通过"),
    APPLY_STATUS_4("4","取消放款"),
    APPLY_STATUS_5("5","确认放款"),
    APPLY_STATUS_6("6","放款中"),
    APPLY_STATUS_7("7","放款成功"),
    APPLY_STATUS_8("8","还款完成"),
    APPLY_STATUS_9("9","逾期"),
    APPLY_STATUS_10("10","放款失败"),
    /**
     * 成功
     */
    SUCCESS("200","成功"),
    /**
     * 系统错误
     */
    SYSTEM_ERROR("500","系统繁忙,请稍后尝试"),
    /**
     * 业务错误
     */
    BIZ_ERROR("400","业务繁忙,请稍后再试"),
    BIZ_ERROR_300("300","账号不存在或密码错误"),
    BIZ_ERROR_301("301","请重新登陆"),
    BIZ_ERROR_302("302","账号已注销"),
    BIZ_ERROR_303("303","账号已存在"),
    BIZ_ERROR_304("304","请更新到最新版本"),
    BIZ_ERROR_305("305","请输入手机号"),
    BIZ_ERROR_306("306", "手机号输入错误"),
    BIZ_ERROR_307("307", "今日操作次数超限,请明日重试!"),
    BIZ_ERROR_401("401", "申请数据已过期,请重新填写"),
    BIZ_ERROR_456("456", "抱歉，目前没有适合您的借贷产品"),
    BIZ_ERROR_456_0("456", "Maaf, saat ini belum ada produk pinjaman yang cocok untuk Anda"),
    BIZ_ERROR_456_1("456", "命中本地黑名单"),
    BIZ_ERROR_456_2("456", "命中三方黑名单"),
    BIZ_ERROR_456_3("456", "没有可用风控渠道"),
    BIZ_ERROR_456_4("456", "三方风控审批拒绝"),
    BIZ_ERROR_456_5("456", "命中黑名单缓存"),
    BIZ_ERROR_456_6("456", "没有可用OCR渠道"),
    BIZ_ERROR_455("455", "您已发送验证码,请直接输入或稍后再试"),
    BIZ_ERROR_457("457", "请获取短信验证码"),
    BIZ_ERROR_458("458", "请输入正确的验证码"),
    BIZ_ERROR_459("459", "短信验证码已失效"),
    BIZ_ERROR_460("460", "账户余额不足，请确认余额在进行提现"),
    /**
     * 参数错误
     */
    PARAM_ERROR("600", "参数错误"),
    TOKEN_CHECK_ERROR("601", "无效请求!"),
    INIT_CHECK_APP("602","请从正规途径下载app"),
    CAPTCHA_CHECK_ERROR("603","验证码错误或已过期!"),
    INVALID_ACCESS_TOKEN("604","invalid access_token"),
    EMAIL_ERROR("605","邮箱格式错误!"),
    /**
     *  产品已停止申请
     */
    PRODUCT_ERROR_700("700","Produk telah berhenti diterapkan"),
    PRODUCT_ERROR_701("701","超出产品总进件数量"),
    PRODUCT_ERROR_702("702","暂时没有可申请产品"),
    PRODUCT_ERROR_703("703","请至少选择一个产品"),
    PRODUCT_ERROR_711("711","用户总在途进件限制"),
    PRODUCT_ERROR_712("712","进件总开关"),
    PRODUCT_ERROR_713("713","您有逾期账单未结清，请结清后借款"),
    PRODUCT_ERROR_716("716","您有订单正在审核中，请稍后借款"),
    AUTH_ERROR_717("717","抱歉,您的人脸检测未通过,请重新认证!"),
    /**
     * 短信错误
     */
    SMS_ERROR_1200("1200","Daily sending limit"),
    ;

    private String status;
    private String message;

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    CodeEnum(String status, String message) {
        this.status = status;
        this.message = message;
    }

    public static CodeEnum convertApiStatus(Integer order_status){
        if(LunduEnum.STATUS_100.getCode().equals(order_status)){
            return CodeEnum.APPLY_STATUS_3;
        }else if(LunduEnum.STATUS_110.getCode().equals(order_status)){
            return CodeEnum.APPLY_STATUS_2;
        }else if(LunduEnum.STATUS_161.getCode().equals(order_status)){
            return CodeEnum.APPLY_STATUS_4;
        }else if(LunduEnum.STATUS_169.getCode().equals(order_status)){
            return CodeEnum.APPLY_STATUS_10;
        }else if(LunduEnum.STATUS_170.getCode().equals(order_status)){
            return CodeEnum.APPLY_STATUS_7;
        }else if(LunduEnum.STATUS_180.getCode().equals(order_status)){
            return CodeEnum.APPLY_STATUS_9;
        }else if(LunduEnum.STATUS_200.getCode().equals(order_status)){
            return CodeEnum.APPLY_STATUS_8;
        }else if(LunduEnum.STATUS_80.getCode().equals(order_status)){
            return CodeEnum.APPLY_STATUS_0;
        }else if(LunduEnum.STATUS_90.getCode().equals(order_status)){
            return CodeEnum.APPLY_STATUS_1;
        }
        // 未知状态不处理
        return null;
    }
}