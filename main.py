note = ""
sender_phone = ""
receiver_phone = ""

while True:
    print("\n===== MENU =====")
    print("1. Nhập dữ liệu đơn hàng và xem báo cáo")
    print("2. Chuẩn hóa mã đơn hàng")
    print("3. Ẩn số điện thoại khách hàng")
    print("4. Tìm kiếm và thay thế từ khóa trong ghi chú")
    print("5. Thoát chương trình")

    choice = input("Nhập lựa chọn: ").strip()

    if not choice.isdigit():
        print("Lựa chọn không hợp lệ.")
        continue

    choice = int(choice)

    if choice < 1 or choice > 5:
        print("Lựa chọn không hợp lệ.")
        continue

    match choice:

        case 1:
            sender_name = input("Nhập tên người gửi: ")
            sender_phone = input("Nhập SĐT người gửi: ")
            pickup_address = input("Nhập địa chỉ lấy hàng: ")

            receiver_name = input("Nhập tên người nhận: ")
            receiver_phone = input("Nhập SĐT người nhận: ")
            delivery_address = input("Nhập địa chỉ giao hàng: ")

            note = input("Nhập ghi chú giao hàng: ")

            if sender_name.strip() == "":
                print("Tên người gửi không được bỏ trống")
                continue

            if sender_phone.strip() == "":
                print("Số điện thoại người gửi không được bỏ trống")
                continue

            if pickup_address.strip() == "":
                print("Địa chỉ lấy hàng không được bỏ trống")
                continue

            if receiver_name.strip() == "":
                print("Tên người nhận không được bỏ trống")
                continue

            if receiver_phone.strip() == "":
                print("Số điện thoại người nhận không được bỏ trống")
                continue

            if delivery_address.strip() == "":
                print("Địa chỉ giao hàng không được bỏ trống")
                continue

            if note.strip() == "":
                print("Ghi chú giao hàng không được bỏ trống")
                continue

            sender_name = sender_name.strip().title()
            receiver_name = receiver_name.strip().title()

            pickup_address = " ".join(pickup_address.split())
            delivery_address = " ".join(delivery_address.split())

            note = note.strip()

            word_count = len(note.split())

            print("\n===== BÁO CÁO ĐƠN HÀNG =====")

            print("Tên người gửi:", sender_name)
            print("Tên người nhận:", receiver_name)

            print("Địa chỉ lấy hàng:", pickup_address)
            print("Địa chỉ giao hàng:", delivery_address)

            print("Ghi chú:", note)

            print("Độ dài ghi chú:", len(note))
            print("Số lượng từ:", word_count)

            print("Ghi chú chữ thường:")
            print(note.lower())

            print("Ghi chú chữ hoa:")
            print(note.upper())

        case 2:
            order_code = input("Nhập mã đơn hàng: ")

            if order_code.strip() == "":
                print("Mã đơn hàng không được bỏ trống")
                continue

            original_code = order_code

            order_code = order_code.strip()
            order_code = order_code.upper()
            order_code = "-".join(order_code.split())

            if not order_code.startswith("GRAB-"):
                order_code = "GRAB-" + order_code

            print("Mã đơn hàng ban đầu:")
            print(original_code)

            print("Mã đơn hàng sau chuẩn hóa:")
            print(order_code)

        case 3:
            if sender_phone.strip() == "" or receiver_phone.strip() == "":
                print("Chưa có dữ liệu số điện thoại.")
                continue

            if not sender_phone.isdigit():
                print("Số điện thoại người gửi không hợp lệ")
                continue

            if len(sender_phone) != 10:
                print("Số điện thoại người gửi không hợp lệ: Số điện thoại phải có đúng 10 ký tự")
                continue

            if not receiver_phone.isdigit():
                print("Số điện thoại người nhận không hợp lệ")
                continue

            if len(receiver_phone) != 10:
                print("Số điện thoại người nhận không hợp lệ: Số điện thoại phải có đúng 10 ký tự")
                continue

            hidden_sender = (
                sender_phone[:3]
                + "*****"
                + sender_phone[-2:]
            )

            hidden_receiver = (
                receiver_phone[:3]
                + "*****"
                + receiver_phone[-2:]
            )

            print("SĐT người gửi:", hidden_sender)
            print("SĐT người nhận:", hidden_receiver)

        case 4:
            if note.strip() == "":
                print("Chưa có ghi chú giao hàng để tìm kiếm")
                continue

            keyword_find = input("Nhập từ khóa cần tìm: ").strip()
            keyword_replace = input("Nhập từ khóa thay thế: ").strip()

            count = note.count(keyword_find)

            if count > 0:
                note = note.replace(
                    keyword_find,
                    keyword_replace
                )

                print("Số lần xuất hiện của từ khóa:", count)

                print("Ghi chú sau khi thay thế:")
                print(note)

            else:
                print("Không tìm thấy từ khóa trong ghi chú")

        case 5:
            print("Thoát chương trình")
            break
