import setuptools

setuptools.setup(
    name = 'async_get_vedio',
    version = '2.1',
    author = 'WUT_ljs',
    author_email = '3480339804@qq.com',
    url = 'https://github.com/wutljs/async_get_vedio',
    description = 'Get vedio',
    long_description = '此次更新,解决了应用pyautogui删除ts文件夹失败的问题;简化了部分程序'
                       '具体文档请进入:https://github.com/wutljs/async_get_vedio 查看.',
    packages = setuptools.find_packages(),
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ]
)