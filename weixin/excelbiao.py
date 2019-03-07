import xlwt
#只能写不能读

shuju = ((13, '徐晓明', '黑LLN260', '2019-03-06 12:26:25', '', '', '小型轿车', '', 'D:githubweixin照片徐晓明122623.jpg'), (14, '徐晓明', '黑K12341', '2019-03-06 12:27:27', '', '', '', '', ''), (15, '徐晓明', '黑K12342', '2019-03-06 12:27:32', '', '', '', '', ''), (16, '徐晓明', '黑K12343', '2019-03-06 12:27:36', '', '', '', '', ''), (17, '徐晓明', '黑K12344', '2019-03-06 12:27:39', '', '', '', '', ''))


book = xlwt.Workbook()#新建一个excel
sheet = book.add_sheet('case1_sheet')#添加一个sheet页
# sheet.write_merge(0, 0, 0, 5)

sheet.col(0).width = 2000
sheet.col(1).width = 2000
sheet.col(2).width = 2500
sheet.col(3).width = 5000
sheet.col(4).width = 5000
sheet.col(5).width = 2500
borders = xlwt.Borders()
borders.left = xlwt.Borders.MEDIUM  # 添加边框-虚线边框
borders.right = xlwt.Borders.MEDIUM  # 添加边框-虚线边框
borders.top = xlwt.Borders.MEDIUM  # 添加边框-虚线边框
borders.bottom = xlwt.Borders.MEDIUM  # 添加边框-虚线边框


style = xlwt.XFStyle()  # Create style
style.borders = borders  # Add borders to style
al = xlwt.Alignment()
al.horz = 0x02      # 设置水平居中
al.vert = 0x01      # 设置垂直居中
style.alignment = al


tall_style = xlwt.easyxf('font:height 720')  # 36pt
first_row = sheet.row(0)
first_row.set_style(tall_style)
tall_style_1 = xlwt.easyxf('font:height 520')  # 36pt
first_row_1 = sheet.row(1)
first_row_1.set_style(tall_style_1)

sheet.write_merge(0, 0, 0, 5,"职工预约车辆登记表（考核办）",style)
sheet.write(1, 0, "序号", style)
sheet.write(1, 1, "姓名", style)
sheet.write(1, 2, "车号", style)
sheet.write(1, 3, "预约时间", style)
sheet.write(1, 4, "检测时间", style)
sheet.write(1, 5, "积分", style)
row = 2#控制行
for stu in shuju:
    print(stu[1:4])
    tall_style_1 = xlwt.easyxf('font:height 520')  # 36pt
    first_row_1 = sheet.row(row)
    first_row_1.set_style(tall_style_1)

    col = 1#控制列
    sheet.write(row, col + 3, "", style)
    sheet.write(row, col + 4, "", style)
    sheet.write(row, 0, row + 1,style)
    for s in stu[1:4]:#再循环里面list的值，每一列
        # sheet.write(row, idhang, str(idhang))
        sheet.write(row,col,s,style)

        col+=1
    row+=1

book.save('stu_1.xls')#保存到当前目录下