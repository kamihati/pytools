import qrcode
import qrcode.image.svg


def make_qrcode(url):
    """
    把指定url声成为二维码图片
    :param url:
    :return:
    """
    img = qrcode.make(url)
    img.save("xinxing.png")
    # version: 二维码版本号，公有1~40个版本号。最小为1，对应21*21,没大一个版本增加4个尺寸单位，是指长宽被分为多少份。不是指长宽。
    # 过高的版本号可能会导致二维码扫码不识别
    # error_correction: 纠错容量，L%7, M 15%(默认), Q 25%, H 30%
    # box_size 生成图片的像素
    # border: 二维码边框宽度，4是最小值
    # image_factory: 继承于qrcode.image.base.BaseImage的类。用于控制make_qrcode()函数返回的图像实例，
    # 可以选择的类保存在模块根目录的image文件夹下。里面有5个py文件，默认使用其中pil.py提供的qrcode.image.pil.PilImage类
    qr = qrcode.QRCode(version=20, error_correction=qrcode.constants.ERROR_CORRECT_M,
                       box_size=10, border=5, image_factory=None)
    qr.add_data(url)
    img = qr.make_image()
    img.save("1_2.png")


def make_svg(method, url):
    """
    生成其它类型的二维码(使用矢量图）
    :param method:
    :param url:
    :return:
    """
    if method == 'basic':
        # 简单的工厂，只有一套
        factory = qrcode.image.svg.SvgImage
    elif method == 'fragment':
        # 碎片工厂（也只是一组矩形）
        factory = qrcode.image.svg.SvgFragmentImage
    else:
        # 组合路径工厂，修复缩放时可能出现的空白
        factory = qrcode.image.svg.SvgPathImage
    img = qrcode.make(url, image_factory=factory)
    # 扩展名不当可能导致图片不可用
    img.save(method + ".svg")


if __name__ == "__main__":
    # make_qrcode('http://www.zut.edu.cn')
    make_svg('basic', 'http://www.zut.edu.cn')
    make_svg('fragment', 'http://www.zut.edu.cn')
    make_svg('svgpath', 'http://www.zut.edu.cn')

