import customtkinter
import tkinter as tk
from customtkinter import CTk
from PIL import Image, ImageTk
from CTkListbox import *
import time
import json
import os

if os.name == "posix":
    homeICO = Image.open("Assets/img/home.png")
    financeICO = Image.open("Assets/img/finance.png")
    searchICO = Image.open("Assets/img/search.png")
    plusICO = Image.open("Assets/img/plus.png")
    minusICO = Image.open("Assets/img/minus.png")
    minusplusICO = Image.open("Assets/img/minusplus.png")
    searchStockICO = Image.open("Assets/img/searchstock.png")
    shopICO = Image.open("Assets/img/shopping.png")
    permICO = Image.open("Assets/img/perm.png")
    cvICO = Image.open("Assets/img/usertable.png")
    jobICO = Image.open("Assets/img/job.png")
    profileICO = Image.open("Assets/img/profile.png")
    userICO = Image.open("Assets/img/user.png")
    refreshICO = Image.open("Assets/img/refresh.png")
    entryICO = Image.open("Assets/img/enter.png")
    clearICO = Image.open("Assets/img/clear.png")
elif os.name == "nt":
    homeICO = Image.open("Assets\\img\\home.png")
    financeICO = Image.open("Assets\\img\\finance.png")
    searchICO = Image.open("Assets\\img\\search.png")
    plusICO = Image.open("Assets\\img\\plus.png")
    minusICO = Image.open("Assets\\img\\minus.png")
    minusplusICO = Image.open("Assets\\img\\minusplus.png")
    searchStockICO = Image.open("Assets\\img\\searchstock.png")
    shopICO = Image.open("Assets\\img\\shopping.png")
    permICO = Image.open("Assets\\img\\perm.png")
    cvICO = Image.open("Assets\\img\\usertable.png")
    jobICO = Image.open("Assets\\img\\job.png")
    profileICO = Image.open("Assets\\img\\profile.png")
    userICO = Image.open("Assets\\img\\user.png")
    refreshICO = Image.open("Assets\\img\\refresh.png")
    entryICO = Image.open("Assets\\img\\enter.png")
    clearICO = Image.open("Assets\\img\\clear.png")

class MarketUi:
    def __init__(self):
        print("[-] LOADING LOGIN UI")
        print("[-] LOADING UI COMPONENTS")
        self.LoginUi = CTk(fg_color="#FCFEFC")
        self.LoginUi.title("Market System")
        self.LoginUi.geometry("400x300")
        self.LoginUi.resizable(False,False)
        self.perms = [
            ("C",    "#FFD2D2",  "Can only perform sales transactions."),
            ("B",    "#FFEFD2",  "Can perform both sales and manage stock."),
            ("A",    "#D2FFD2",  "Has access to the finance window."),
            ("A+",   "#D2F0FF",  "Extended financial access and reports."),
            ("A++",  "#D2D2FF",  "Advanced financial tools and audits."),
            ("S",    "#E0D2FF",  "Full access to all admin panels."),
            ("S+",   "#FFD2F2",  "Can create, edit, and remove users."),
        ]    

        LoginFrame = customtkinter.CTkFrame(self.LoginUi,
                                            width=350,
                                            height=250,
                                            fg_color="#C3D8D5")
        LoginFrame.place(x=25,y=25)

        LoginTitle = customtkinter.CTkLabel(LoginFrame,
                                            text="Login",
                                            font=("Helvetica",20,"bold"),
                                            text_color="#000000")
        
        LoginTitle.place(x=150,y=10)

        LN_LocalLabel = customtkinter.CTkLabel(LoginFrame,
                                               text="Name",
                                               font=("Sans-Serif",15),
                                               text_color="#171717")
        LN_LocalLabel.place(x=30,y=40)

        LN_LocalEntry = customtkinter.CTkEntry(LoginFrame,
                                               placeholder_text="Enter User Name",
                                               placeholder_text_color="#444343",
                                               fg_color="#F2FDFD",
                                               text_color="#000000",
                                               font=("Default", 15),
                                               corner_radius=10,
                                               border_width=0,
                                               width=300,
                                               height=40)
        
        LN_LocalEntry.place(x=25,y=70)


        LP_LocalLabel = customtkinter.CTkLabel(LoginFrame,
                                               text="Password",
                                               font=("Sans-Serif",15),
                                               text_color="#171717")
        LP_LocalLabel.place(x=30,y=110)

        LP_LocalEntry = customtkinter.CTkEntry(LoginFrame,
                                               placeholder_text="Enter Password",
                                               placeholder_text_color="#444343",
                                               fg_color="#F2FDFD",
                                               text_color="#000000",
                                               font=("Default", 15),
                                               corner_radius=10,
                                               border_width=0,
                                               width=300,
                                               height=40,
                                               show="*")
        
        LP_LocalEntry.place(x=25,y=140)



        LPR_LocalButton = customtkinter.CTkButton(LoginFrame,
                                                  text="Login",
                                                  width=100,
                                                  height=40,
                                                  corner_radius=10,
                                                  fg_color="#33FA62",
                                                  hover_color="#2DE157",
                                                  text_color="#000000",
                                                  font=("Default",15,"bold"),
                                                  command=lambda:self.LoadMainUi(EnteredName=LN_LocalEntry.get(), EnteredPass=LP_LocalEntry.get()))


        LPR_LocalButton.place(x=125,y=200)
        print("[OK] LOADED LOGIN UI")


    def LoadData(self,jsonP):
        with open(jsonP) as f:
            self.JsonData = json.load(f)


    def perm_num_to_str(self, Perm):
        # Perm sayısal ise harfe çevirir
        if not isinstance(Perm, int):
            try:
                Perm = int(Perm)
            except:
                return "Unknown"
        if Perm == 1:
            return "C"
        elif Perm == 2:
            return "B"
        elif Perm == 3:
            return "A"
        elif Perm == 4:
            return "A+"
        elif Perm == 5:
            return "A++"
        elif Perm == 6:
            return "S"
        elif Perm >= 7:
            return "S+"
        else:
            return "Unknown"

    def perm_str_to_num(self, perm_str):
        perm_map = {
            "C": 1,
            "B": 2,
            "A": 3,
            "A+": 4,
            "A++": 5,
            "S": 6,
            "S+": 7
        }
        return perm_map.get(perm_str.upper(), 0)

    def SetPerm(self, Perm):
            if Perm == 1:
                return "C"
            elif Perm == 2:
                return "B"
            elif Perm == 3:
                return "A"
            elif Perm == 4:
                return "A+"
            elif Perm == 5:
                return "A++"
            elif Perm == 6:
                return "S"
            elif Perm >= 7:
                return "S+"
            elif Perm == "C":
                return 1
            elif Perm == "B":
                return 2
            elif Perm == "A":
                return 3
            elif Perm == "A+":
                return 4
            elif Perm == "A++":
                return 5
            elif Perm == "S":
                return 6
            elif Perm == "S+":
                return 7

    def scrollEnter(self, event):
        if event.num == 5 or event.delta < 0:
            self.DocsFrame._parent_canvas.yview_scroll(1, "units")
        elif event.num == 4 or event.delta > 0:
            self.DocsFrame._parent_canvas.yview_scroll(-1, "units")
    def changeNew(self, NewName, NewPassword, NewPerm):
        path = "Assets/data/UserManagement.json" if os.name == "posix" else "Assets\\data\\UserManagement.json"
        with open(path, "r") as f:
            data = json.load(f)

        current_user_data = data.get(self.LoginName, {})
        if NewPassword:
            current_user_data["Password"] = NewPassword
        if NewPerm:
            current_user_data["Perm"] = self.perm_str_to_num(NewPerm)
        if NewName and NewName != self.LoginName:
            current_user_data["UserName"] = NewName
            data[NewName] = current_user_data
            del data[self.LoginName]
            self.LoginName = NewName
        else:
            data[self.LoginName] = current_user_data

        with open(path, "w") as f:
            json.dump(data, f, indent=4)

        self.LoadData(jsonP=path)

        self.LN_LocalEntry.delete(0, "end")
        self.LP_LocalEntry.delete(0, "end")
        self.LN_LocalEntry.configure(placeholder_text=self.JsonData[self.LoginName]["UserName"])
        self.LP_LocalEntry.configure(placeholder_text=self.JsonData[self.LoginName]["Password"])
        self.LN_LocalEntry.insert(0, self.JsonData[self.LoginName]["UserName"])
        self.LP_LocalEntry.insert(0, self.JsonData[self.LoginName]["Password"])

    def deleteUser(self):
        username_to_delete = self.listbox.get()
        import os, json
        path = "Assets/data/UserManagement.json" if os.name == "posix" else "Assets\\data\\UserManagement.json"

        with open(path, "r") as f:
            data = json.load(f)

        if username_to_delete in data:
            del data[username_to_delete]
            with open(path, "w") as f:
                json.dump(data, f, indent=4)

            self.LoadData(jsonP=path)

            self.LN_LocalEntry.delete(0, "end")
            self.LP_LocalEntry.delete(0, "end")
            self.LN_LocalEntry.configure(placeholder_text="")
            self.LP_LocalEntry.configure(placeholder_text="")
            self.UserHomeUi.destroy()
            self.RefListBox()

    def RefListBox(self):
        print("[OK] Refresh User List")
        try:
            self.listbox.delete(0, "end")
            if os.name == "posix":
                pathJ = "Assets/data/UserManagement.json"
            elif os.name == "nt":
                pathJ = "Assets\\data\\UserManagement.json"

            with open(pathJ, "r") as f:
                datas = json.load(f)
                for key in datas.keys():
                    self.listbox.insert("end", key)
        except Exception as e:
            self.listbox.insert("end", f"Error: {e}")


    def onSelect(self,selectedDropDown):
        if selectedDropDown == "C":
            self.SelectedPerm = "C"
        elif selectedDropDown == "B":
            self.SelectedPerm = "B"
        elif selectedDropDown == "A":
            self.SelectedPerm = "A"
        elif selectedDropDown == "A+":
            self.SelectedPerm = "A+"
        elif selectedDropDown == "A++":
            self.SelectedPerm = "A++"
        elif selectedDropDown == "S":
            self.SelectedPerm = "S"
        elif selectedDropDown == "S+":
            self.SelectedPerm = "S+"
    def LoadUserHomeUi(self,selectedIndex):
        if os.name == "posix":
            self.LoadData(jsonP="Assets/data/UserManagement.json")
        elif os.name == "nt":
            self.LoadData(jsonP="Assets\\data\\UserManagement.json")

        if self.JsonData[self.LoginName]["Perm"] < 7:
            return
        else:
            pass
        self.UserHomeUi = customtkinter.CTkToplevel(self.MainUi,fg_color="#FFFFFF")
        self.UserHomeUi.title("Market Ui System")
        self.UserHomeUi.resizable(False,False)
        self.UserHomeUi.geometry("600x300")
        if os.name == "nt":self.UserHomeUi.grab_set()

        UserFrame = customtkinter.CTkFrame(self.UserHomeUi,
                                            width=550,
                                            height=250,
                                            fg_color="#C3D8D5")
        UserFrame.place(x=25,y=25)

        UserTitle = customtkinter.CTkLabel(UserFrame,
                                            text="User",
                                            font=("Helvetica",20,"bold"),
                                            text_color="#000000")
        
        UserTitle.place(x=250,y=10)

        LN_LocalLabel = customtkinter.CTkLabel(UserFrame,
                                               text="Name",
                                               font=("Sans-Serif",15),
                                               text_color="#171717")
        LN_LocalLabel.place(x=30,y=40)

        self.LN_LocalEntry = customtkinter.CTkEntry(UserFrame,
                                               placeholder_text=self.JsonData[selectedIndex]["UserName"],
                                               placeholder_text_color="#000000",
                                               fg_color="#F2FDFD",
                                               text_color="#000000",
                                               font=("Default", 15),
                                               corner_radius=10,
                                               border_width=0,
                                               width=300,
                                               height=40)
        
        self.LN_LocalEntry.place(x=25,y=70)
        self.LN_LocalEntry.insert(0,self.JsonData[selectedIndex]["UserName"])


        LP_LocalLabel = customtkinter.CTkLabel(UserFrame,
                                               text="Password",
                                               font=("Sans-Serif",15),
                                               text_color="#171717")
        LP_LocalLabel.place(x=30,y=110)

        self.LP_LocalEntry = customtkinter.CTkEntry(UserFrame,
                                               placeholder_text=self.JsonData[selectedIndex]["Password"],
                                               placeholder_text_color="#000000",
                                               fg_color="#F2FDFD",
                                               text_color="#000000",
                                               font=("Default", 15),
                                               corner_radius=10,
                                               border_width=0,
                                               width=300,
                                               height=40,
                                               show="*")
        
        self.LP_LocalEntry.place(x=25,y=140)
        self.LP_LocalEntry.insert(0,self.JsonData[selectedIndex]["Password"])



        LPR_LocalButton = customtkinter.CTkButton(UserFrame,
                                                  text="Save",
                                                  width=100,
                                                  height=40,
                                                  corner_radius=10,
                                                  fg_color="#33FA62",
                                                  hover_color="#2DE157",
                                                  text_color="#000000",
                                                  font=("Default",15,"bold"),
                                                  command=lambda:self.changeNew(NewName=self.LN_LocalEntry.get(), NewPassword=self.LP_LocalEntry.get(), NewPerm=dropdown.get()))


        LPR_LocalButton.place(x=170,y=200)


        LN_LocalsLabel = customtkinter.CTkLabel(UserFrame,
                                               text="Permission",
                                               font=("Sans-Serif",15),
                                               text_color="#171717")
        LN_LocalsLabel.place(x=360,y=100)


        dropdown = customtkinter.CTkOptionMenu(
            master=UserFrame,
            values=["C", "B", "A", "A+", "A++", "S", "S+"],
            fg_color="#ECEAEA",
            corner_radius=5,
            button_color="#E0DFDF",
            text_color="#000000",
            button_hover_color="#D4D1D1",
            dropdown_text_color="#000000",
            dropdown_fg_color="#ECEAEA",
            command=self.onSelect
        )
        dropdown.place(x=355,y=125)


        LPD_LocalButton = customtkinter.CTkButton(UserFrame,
                                                  text="Delete",
                                                  width=100,
                                                  height=40,
                                                  corner_radius=10,
                                                  fg_color="#FE3939",
                                                  hover_color="#EC3434",
                                                  text_color="#000000",
                                                  font=("Default",15,"bold"),
                                                  command=self.deleteUser)


        LPD_LocalButton.place(x=280,y=200)


    def CreateUser(self, CreateName,CreatePass,CreatePerm,CreateJob):
        path = "Assets/data/UserManagement.json" if os.name == "posix" else "Assets\\data\\UserManagement.json"
        with open(path, "r") as f:
            data = json.load(f)

        data[CreateName] = {
            "UserName" : CreateName,
            "Password" : CreatePass,
            "Perm" : self.perm_str_to_num(CreatePerm),
            "Job" : CreateJob
        }

        with open(path,"w") as f:
            json.dump(data,f,indent=4)

        self.UserCHomeUi.destroy()

    def LoadCreateHomeUi(self):
        if os.name == "posix":
            self.LoadData(jsonP="Assets/data/UserManagement.json")
        elif os.name == "nt":
            self.LoadData(jsonP="Assets\\data\\UserManagement.json")

        if self.JsonData[self.LoginName]["Perm"] < 7:
            return
        else:
            pass
        self.UserCHomeUi = customtkinter.CTkToplevel(self.MainUi,fg_color="#FFFFFF")
        self.UserCHomeUi.title("Market Ui System")
        self.UserCHomeUi.resizable(False,False)
        self.UserCHomeUi.geometry("600x300")
        if os.name == "nt":self.UserHomeUi.grab_set()

        UserCFrame = customtkinter.CTkFrame(self.UserCHomeUi,
                                            width=550,
                                            height=250,
                                            fg_color="#C3D8D5")
        UserCFrame.place(x=25,y=25)

        UserCTitle = customtkinter.CTkLabel(UserCFrame,
                                            text="User",
                                            font=("Helvetica",20,"bold"),
                                            text_color="#000000")
        
        UserCTitle.place(x=250,y=10)

        LNC_LocalLabel = customtkinter.CTkLabel(UserCFrame,
                                               text="Name",
                                               font=("Sans-Serif",15),
                                               text_color="#171717")
        LNC_LocalLabel.place(x=30,y=40)

        self.LNC_LocalEntry = customtkinter.CTkEntry(UserCFrame,
                                               placeholder_text="",
                                               placeholder_text_color="#000000",
                                               fg_color="#F2FDFD",
                                               text_color="#000000",
                                               font=("Default", 15),
                                               corner_radius=10,
                                               border_width=0,
                                               width=300,
                                               height=40)
        
        self.LNC_LocalEntry.place(x=25,y=70)


        LPC_LocalLabel = customtkinter.CTkLabel(UserCFrame,
                                               text="Password",
                                               font=("Sans-Serif",15),
                                               text_color="#171717")
        LPC_LocalLabel.place(x=30,y=110)

        self.LPC_LocalEntry = customtkinter.CTkEntry(UserCFrame,
                                               placeholder_text="",
                                               placeholder_text_color="#000000",
                                               fg_color="#F2FDFD",
                                               text_color="#000000",
                                               font=("Default", 15),
                                               corner_radius=10,
                                               border_width=0,
                                               width=300,
                                               height=40,
                                               show="*")
        
        self.LPC_LocalEntry.place(x=25,y=140)
        LPRC_LocalButton = customtkinter.CTkButton(UserCFrame,
                                                  text="Create",
                                                  width=100,
                                                  height=40,
                                                  corner_radius=10,
                                                  fg_color="#33FA62",
                                                  hover_color="#2DE157",
                                                  text_color="#000000",
                                                  font=("Default",15,"bold"),
                                                  command=lambda:self.CreateUser(CreateName=self.LNC_LocalEntry.get(), CreatePass=self.LPC_LocalEntry.get(),CreateJob=dropCdown2.get(),CreatePerm=dropCdown.get()))


        LPRC_LocalButton.place(x=170,y=200)


        LNC_LocalsLabel = customtkinter.CTkLabel(UserCFrame,
                                               text="Permission",
                                               font=("Sans-Serif",15),
                                               text_color="#171717")
        LNC_LocalsLabel.place(x=360,y=40)


        dropCdown = customtkinter.CTkOptionMenu(
            master=UserCFrame,
            values=["C", "B", "A", "A+", "A++", "S", "S+"],
            fg_color="#ECEAEA",
            corner_radius=5,
            button_color="#E0DFDF",
            text_color="#000000",
            button_hover_color="#D4D1D1",
            dropdown_text_color="#000000",
            dropdown_fg_color="#ECEAEA"
        )
        dropCdown.place(x=355,y=75)

        LN2_LocalsLabel = customtkinter.CTkLabel(UserCFrame,
                                               text="Job",
                                               font=("Sans-Serif",15),
                                               text_color="#171717")
        LN2_LocalsLabel.place(x=360,y=110)
        dropCdown2 = customtkinter.CTkOptionMenu(
            master=UserCFrame,
            values=["Cashier",
                    "Financer",
                    "CEO",
                    "Admin",
                    "Technic Support",
                    "Intern",
                    "Market Expert",
                    "Manager"],
            fg_color="#ECEAEA",
            corner_radius=5,
            button_color="#E0DFDF",
            text_color="#000000",
            button_hover_color="#D4D1D1",
            dropdown_text_color="#000000",
            dropdown_fg_color="#ECEAEA"
        )
        dropCdown2.place(x=355,y=145)    

    def EVENT_LIST_TO_LIST(self,selectedIndex):
        self.AddedItemslistbox.insert("end", selectedIndex)
        Path = "Assets/data/Payment.json" if os.name == "posix" else "Assets\\data\\Payment.json"

        if not os.path.exists(Path) or os.stat(Path).st_size == 0:
            with open(Path, "w") as f:
                json.dump({}, f)
        with open(Path, "r") as f:
            try:
                jsdata = json.load(f)
            except json.JSONDecodeError:
                jsdata = {}


        if selectedIndex in jsdata:
            jsdata[selectedIndex]["Count"] += 1
        else:
            jsdata[selectedIndex] = {"Count": 1}

        with open(Path, "w") as f:
            json.dump(jsdata, f, indent=4)

        self.EVENT_LOADBILLS()


    def EVENT_LOADBILLS(self):
        try:
            self.BillListbox.delete(0, "end")
            path_payment = "Assets/data/Payment.json" if os.name == "posix" else "Assets\\data\\Payment.json"
            path_items = "Assets/data/Item.json" if os.name == "posix" else "Assets\\data\\Item.json"

            with open(path_payment, "r") as f:
                payment_data = json.load(f)

            with open(path_items, "r") as f:
                item_data = json.load(f)
            self.BillListbox.delete(0, "end")
            for product_name, values in payment_data.items():
                count = values.get("Count", 0)

                product_info = item_data.get(product_name)
                if product_info:
                    price = product_info.get("Price", 0)
                    total_price = count * price
                    self.BillListbox.insert("end", f"{product_name} || {total_price}₺")
                else:
                    self.BillListbox.insert("end", f"{product_name} || Not Found Item")

        except Exception as e:
            pass


    def EVENT_CLEARLIST(self):
        Path = "Assets/data/Payment.json" if os.name == "posix" else "Assets\\data\\Payment.json"
        with open(Path, "w") as f:
            json.dump({},f)
        print("[OK] Refresh Item List")
        try:
            self.AddedItemslistbox.delete(0, "end")
            if os.name == "posix":
                pathJ = "Assets/data/Payment.json"
            elif os.name == "nt":
                pathJ = "Assets\\data\\Payment.json"

            with open(pathJ, "r") as f:
                datas = json.load(f)
                for key in datas.keys():
                    self.AddedItemslistbox.insert("end", key)
        except Exception as e:
            self.AddedItemslistbox.insert("end", f"Error: {e}")

        self.EVENT_LOADBILLS()


    def EVENT_GETITEM(self):
        path_itemid = "Assets/data/ItemID.json" if os.name == "posix" else "Assets\\data\\ItemID.json"
        path_payment = "Assets/data/Payment.json" if os.name == "posix" else "Assets\\data\\Payment.json"

        input_id = self.LENTRY.get().strip()
        with open(path_itemid, "r") as f:
            items = json.load(f)

        if input_id in items:
            item_name = items[input_id]["Name"]
            self.AddedItemslistbox.insert("end", item_name)

            if not os.path.exists(path_payment) or os.stat(path_payment).st_size == 0:
                with open(path_payment, "w") as f:
                    json.dump({}, f)

            with open(path_payment, "r") as f:
                try:
                    jsdata = json.load(f)
                except json.JSONDecodeError:
                    jsdata = {}

            if item_name in jsdata:
                jsdata[item_name]["Count"] += 1
            else:
                jsdata[item_name] = {"Count": 1}

            with open(path_payment, "w") as f:
                json.dump(jsdata, f, indent=4)

            self.EVENT_LOADBILLS()
        else:
            print(f"[ERR] Error :  Not Found Item On This Id --> {input_id}")


    def EVENT_DELETEITEM(self,selectedSTRINDEX):
        path_payment = "Assets/data/Payment.json" if os.name == "posix" else "Assets\\data\\Payment.json"

        with open(path_payment, "r") as f:
            itemload = json.load(f)

        if selectedSTRINDEX in itemload:
            if itemload[selectedSTRINDEX]["Count"] > 1:
                itemload[selectedSTRINDEX]["Count"] -= 1
            else:
                del itemload[selectedSTRINDEX]
            with open(path_payment, "w") as f:
                json.dump(itemload, f, indent=4)

            self.AddedItemslistbox.delete(self.AddedItemslistbox.curselection())

        self.EVENT_LOADBILLS()
            


        

    def EVENT_LOADSHOP(self):                                                                                     
        print("[-] LOADING SHOP PAGE")
        self.ListPayment = 0
        self.ShopUiFrame.tkraise()
        self.ShopUiFrame.place(x=205,y=0)
        Path = "Assets/data/Payment.json" if os.name == "posix" else "Assets\\data\\Payment.json"
        with open(Path, "w") as f:
            json.dump({},f)

        ItemIDFrame = customtkinter.CTkFrame(self.ShopUiFrame,
                                             width=325,
                                             height=125,
                                             fg_color="#e1dcdc",
                                             corner_radius=5,
                                             border_width=1,
                                             border_color="#bfbcbc")
        ItemIDFrame.place(x=50,y=100)


        self.FastItemlistbox = CTkListbox(self.ShopUiFrame, width=250, height=325, border_width=1, font=("Default", 20,"bold"),border_color="#888888",fg_color="#EDEDED",command=self.EVENT_LIST_TO_LIST,text_color="#000000",hover_color="#e3e3e3")
        self.FastItemlistbox.place(x=450,y=100)

        self.AddedItemslistbox = CTkListbox(self.ShopUiFrame, width=300, height=250, border_width=1, font=("Default", 20,"bold"),border_color="#888888",fg_color="#EDEDED",command=self.EVENT_DELETEITEM,text_color="#000000",hover_color="#e3e3e3")
        self.AddedItemslistbox.place(x=50,y=250)

        self.BillListbox = CTkListbox(self.ShopUiFrame, width=250, height=125, border_width=1, font=("Default", 20,"bold"),border_color="#888888",fg_color="#EDEDED",text_color="#000000",hover_color="#e3e3e3")
        self.BillListbox.place(x=450,y=450) 


        try:
            path_payment = "Assets/data/Payment.json" if os.name == "posix" else "Assets\\data\\Payment.json"
            path_items = "Assets/data/Item.json" if os.name == "posix" else "Assets\\data\\Item.json"

            with open(path_payment, "r") as f:
                payment_data = json.load(f)

            with open(path_items, "r") as f:
                item_data = json.load(f)
            self.BillListbox.delete(0, "end")
            for product_name, values in payment_data.items():
                count = values.get("Count", 0)

                product_info = item_data.get(product_name)
                if product_info:
                    price = product_info.get("Price", 0)
                    total_price = count * price
                    self.BillListbox.insert("end", f"{product_name} || {total_price}₺")
                else:
                    self.BillListbox.insert("end", f"{product_name} || Ürün Bulunamadı")

        except Exception as e:
            print(f"[ERR] Error : {e}")

        try:
            if os.name == "posix":
                pathJ = "Assets/data/FastItem.json"
            elif os.name == "nt":
                pathJ = "Assets\\data\\FastItem.json"
            with open(pathJ, "r") as f:
                datas = json.load(f)
                for key in datas.keys():
                    self.FastItemlistbox.insert("end", key)
        except Exception as e:
            self.FastItemlistbox.insert("end", f"Error: {e}")

        UserPageTitle = customtkinter.CTkLabel(self.ShopUiFrame,
                                               text="Shop Page",
                                               text_color="#000000",
                                               font=("Helvetica", 20, "bold"))
        UserPageTitle.place(x=300,y=20)

        LENTRYLabel = customtkinter.CTkLabel(ItemIDFrame,
                                        text="Item ID",
                                        text_color="#000000",
                                        font=("Default", 15, "bold"))
        
        LENTRYLabel.place(x=15,y=15)

        self.LENTRY = customtkinter.CTkEntry(ItemIDFrame,
                                        placeholder_text="Enter Item ID",
                                        placeholder_text_color="#A1A1A1",
                                        width=250,
                                        height=40,
                                        fg_color="#EEEEEE",
                                        text_color="#000000")
        
        self.LENTRY.place(x=10,y=40)

        LENTRYButton = customtkinter.CTkButton(ItemIDFrame,
                                               text="",
                                               font=("Default", 15,"bold"),
                                               image=customtkinter.CTkImage(dark_image=entryICO,size=(32,32)),
                                               width=25,
                                               height=40,
                                               fg_color="#0EDB1C",
                                               hover_color="#0EC41A",
                                               command=self.EVENT_GETITEM)
        LENTRYButton.place(x=270,y=40)


        LENTRYsButton = customtkinter.CTkButton(self.ShopUiFrame,
                                               text="",
                                               font=("Default", 15,"bold"),
                                               image=customtkinter.CTkImage(dark_image=clearICO,size=(32,32)),
                                               width=275,
                                               height=40,
                                               fg_color="#0EDB1C",
                                               hover_color="#0EC41A",
                                               command=self.EVENT_CLEARLIST)
        LENTRYsButton.place(x=50,y=520)

        LENTRYssButton = customtkinter.CTkButton(self.ShopUiFrame,
                                               text="",
                                               font=("Default", 15,"bold"),
                                               image=customtkinter.CTkImage(dark_image=refreshICO,size=(32,32)),
                                               width=50,
                                               height=40,
                                               fg_color="#0EDB1C",
                                               hover_color="#0EC41A",
                                               command=self.EVENT_LOADBILLS)
        LENTRYssButton.place(x=325,y=520)


        print("[OK] LOADED SHOP PAGE")


    def EVENT_LOADHOME(self):
        self.HomUiFrame.tkraise()
        self.HomUiFrame.place(x=205,y=5)

    def LoadMainUi(self, EnteredPass, EnteredName):
        print(f"""
[!] ENTERED NAME : {EnteredName}
[!] ENTERED PASSWORD : {EnteredPass}
[-] CHECKING ...

              """)
        if os.name == "posix":
            self.LoadData(jsonP="Assets/data/UserManagement.json")
        elif os.name == "nt":
            self.LoadData(jsonP="Assets\\data\\UserManagement.json")
        
        if EnteredName in self.JsonData:
            print("[OK] NAME VALIDATION SUCCES")
            if EnteredPass == self.JsonData[EnteredName]["Password"]:
                print("[OK] PASSWORD VALIDATION SUCCES")
                print("[OK] LOADING MAIN UI")
            else:
                print("[NO] PASSWORD VALIDATION UNSUCCES")
                return
            
        else:
            print("[NO] NAME VALIDATION UNSUCCES")
            return
        
        self.LoginName = EnteredName
        self.LoginPass = EnteredPass
        
        self.LoginUi.destroy()
        print("[-] LOADING MAIN UI")
        print("[-] LOADING MAIN UI COMPONENTS")

        self.MainUi = CTk(fg_color="#FFFFFF")
        self.MainUi.title("Market System")
        self.MainUi.geometry("960x600")
        self.MainUi.resizable(False,False)

        self.HomUiFrame = customtkinter.CTkFrame(self.MainUi, width=750,height=600, fg_color="#FFFFFF")
        self.ShopUiFrame = customtkinter.CTkFrame(self.MainUi, width=750,height=600, fg_color="#FFFFFF")

        self.HomUiFrame.place(x=205,y=0)
        self.HomUiFrame.tkraise()

        # HOME COMPONENTS
        if os.name == "posix":
            self.LoadData(jsonP="Assets/data/UserManagement.json")
        elif os.name == "nt":
            self.LoadData(jsonP="Assets\\data\\UserManagement.json")


        loadedUserINFrame = customtkinter.CTkFrame(self.HomUiFrame,fg_color="#EDEDED",width=425,height=150,border_width=1,border_color="#bcb8b8")
        loadedUserINFrame.place(x=5,y=125)

        self.DocsFrame = customtkinter.CTkScrollableFrame(self.HomUiFrame,fg_color="#EDEDED",width=400,height=150,border_width=1,border_color="#bcb8b8")
        self.DocsFrame.place(x=5,y=300)
        self.DocsFrame.bind_all("<MouseWheel>", self.scrollEnter)  # Windows/macOS
        self.DocsFrame.bind_all("<Button-4>", self.scrollEnter)    # Linux (scroll up)
        self.DocsFrame.bind_all("<Button-5>", self.scrollEnter)    # Linux (scroll down)


        IdentityImage = customtkinter.CTkLabel(loadedUserINFrame,
                                               text="",
                                               image=customtkinter.CTkImage(light_image=profileICO,size=(24,24)),
                                               )
        IdentityImage.place(x=200,y=5)     

        UserNameLabel = customtkinter.CTkLabel(loadedUserINFrame,
                                               text=f"{self.JsonData[EnteredName]['UserName']}",
                                               image=customtkinter.CTkImage(light_image=cvICO,size=(48,48)),
                                               compound="top",
                                               text_color="#000000",
                                               font=("Default",18,"bold"))
        UserNameLabel.place(x=325,y=45)

        UserJobLabel = customtkinter.CTkLabel(loadedUserINFrame,
                                               text=f"{self.JsonData[EnteredName]['Job']}",
                                               image=customtkinter.CTkImage(light_image=jobICO,size=(48,48)),
                                               compound="top",
                                               text_color="#000000",
                                               font=("Default",18,"bold"))
        UserJobLabel.place(x=40,y=45)

        Perm = self.SetPerm(self.JsonData[EnteredName]['Perm'])
        UserPermLabel = customtkinter.CTkLabel(loadedUserINFrame,
                                               text=f"{Perm}",
                                               image=customtkinter.CTkImage(light_image=permICO,size=(48,48)),
                                               compound="top",
                                               text_color="#000000",
                                               font=("Default",18,"bold"))
        UserPermLabel.place(x=190,y=45)
         
        for level, color, desc in self.perms:
            frame = customtkinter.CTkFrame(self.DocsFrame, fg_color=color, corner_radius=6)
            frame.pack(fill="x", padx=5, pady=3)
            label = customtkinter.CTkLabel(frame,
                                text=f"{level} : {desc}",
                                anchor="w",
                                font=("Arial", 12),
                                text_color="#000000")
            label.pack(padx=10, pady=4, fill="x")

        self.listbox = CTkListbox(self.HomUiFrame, width=250, height=300, border_width=1, font=("Default", 20,"bold"),border_color="#888888",fg_color="#EDEDED",command=self.LoadUserHomeUi,text_color="#000000",hover_color="#e3e3e3")
        self.listbox.place(x=450,y=125)

        try:
   
            if os.name == "posix":
                pathJ = "Assets/data/UserManagement.json"
            elif os.name == "nt":
                pathJ = "Assets\\data\\UserManagement.json"

            with open(pathJ, "r") as f:
                datas = json.load(f)
                for key in datas.keys():
                    self.listbox.insert("end", key)
        except Exception as e:
            self.listbox.insert("end", f"Error: {e}")


        HomeUserAdd = customtkinter.CTkButton(self.HomUiFrame,
                                                    text="New User",
                                                    text_color="#000000",
                                                    font=("Helvetica", 15, "bold"),
                                                    fg_color="#F8F4F4",
                                                    hover_color="#ECECEC",
                                                    corner_radius=5,
                                                    width=200,
                                                    height=40,
                                                    anchor="w",
                                                    image=customtkinter.CTkImage(light_image=userICO, size=(32,32)),
                                                    compound="left",
                                                    command=self.LoadCreateHomeUi
                                                    )

        HomeUserAdd.place(x=450,y=450)

        HomeListRef = customtkinter.CTkButton(self.HomUiFrame,
                                                    text="",
                                                    text_color="#000000",
                                                    font=("Helvetica", 15, "bold"),
                                                    fg_color="#F8F4F4",
                                                    hover_color="#ECECEC",
                                                    corner_radius=5,
                                                    width=55,
                                                    height=40,
                                                    image=customtkinter.CTkImage(light_image=refreshICO, size=(32,32)),
                                                    command=self.RefListBox
                                                    )

        HomeListRef.place(x=670,y=450)

        MainPageTitle = customtkinter.CTkLabel(self.HomUiFrame,
                                               text="Home Page",
                                               text_color="#000000",
                                               font=("Helvetica", 20, "bold"))
        


        MainPageTitle.place(x=300,y=20)



        # LEFT FRAME COMPONENTS
        LeftFrameLabel = customtkinter.CTkFrame(self.MainUi,width=2, height=970,corner_radius=0,fg_color="#A4A0A0")
        LeftFrameLabel.place(x=200,y=0)

        LFrameTitle = customtkinter.CTkLabel(self.MainUi,
                                             text="Market App",
                                             font=("Helvetica", 19, "bold"),
                                             text_color="#000000")
        
        LFrameTitle.place(x=15,y=10)

        LFrameSCTitle = customtkinter.CTkLabel(self.MainUi,
                                             text="Management",
                                             font=("Default", 15),
                                             text_color="#000000")
        
        LFrameSCTitle.place(x=17,y=90)

        LFrameTHRTitle = customtkinter.CTkLabel(self.MainUi,
                                             text="Shopping",
                                             font=("Default", 15),
                                             text_color="#000000")
        
        LFrameTHRTitle.place(x=17,y=310)

        LFrameMainPButton = customtkinter.CTkButton(self.MainUi,
                                                    text="Home",
                                                    text_color="#000000",
                                                    font=("Helvetica", 15, "bold"),
                                                    fg_color="#F8F4F4",
                                                    hover_color="#ECECEC",
                                                    corner_radius=5,
                                                    width=175,
                                                    height=40,
                                                    anchor="w",
                                                    image=customtkinter.CTkImage(light_image=homeICO, size=(32,32)),
                                                    compound="left",
                                                    command=self.EVENT_LOADHOME
                                                    )
        LFrameMainPButton.place(x=15,y=120)
        
        LFrameSearchPButton = customtkinter.CTkButton(self.MainUi,
                                                    text="Search",
                                                    text_color="#000000",
                                                    font=("Helvetica", 15, "bold"),
                                                    fg_color="#F8F4F4",
                                                    hover_color="#ECECEC",
                                                    corner_radius=5,
                                                    width=175,
                                                    height=40,
                                                    anchor="w",
                                                    image=customtkinter.CTkImage(light_image=searchICO, size=(32,32)),
                                                    compound="left"
                                                    )

        LFrameSearchPButton.place(x=15,y=170)  


        LFrameCiroPButton = customtkinter.CTkButton(self.MainUi,
                                                    text="Finance",
                                                    text_color="#000000",
                                                    font=("Helvetica", 15, "bold"),
                                                    fg_color="#F8F4F4",
                                                    hover_color="#ECECEC",
                                                    corner_radius=5,
                                                    width=175,
                                                    height=40,
                                                    anchor="w",
                                                    image=customtkinter.CTkImage(light_image=financeICO, size=(32,32)),
                                                    compound="left"
                                                    )

        LFrameCiroPButton.place(x=15,y=220)


        LFrameStockPButton = customtkinter.CTkButton(self.MainUi,
                                                    text="Manage Stocks",
                                                    text_color="#000000",
                                                    font=("Helvetica", 15, "bold"),
                                                    fg_color="#F8F4F4",
                                                    hover_color="#ECECEC",
                                                    corner_radius=5,
                                                    width=175,
                                                    height=40,
                                                    anchor="w",
                                                    image=customtkinter.CTkImage(light_image=minusplusICO, size=(32,32)),
                                                    compound="left"
                                                    )

        LFrameStockPButton.place(x=15,y=350)


        LFrameSearchStocksPButton = customtkinter.CTkButton(self.MainUi,
                                                    text="Search Stocks",
                                                    text_color="#000000",
                                                    font=("Helvetica", 15, "bold"),
                                                    fg_color="#F8F4F4",
                                                    hover_color="#ECECEC",
                                                    corner_radius=5,
                                                    width=175,
                                                    height=40,
                                                    anchor="w",
                                                    image=customtkinter.CTkImage(light_image=searchStockICO, size=(32,32)),
                                                    compound="left"
                                                    )

        LFrameSearchStocksPButton.place(x=15,y=400)


        LFrameShopButton = customtkinter.CTkButton(self.MainUi,
                                                    text="Shop",
                                                    text_color="#000000",
                                                    font=("Helvetica", 15, "bold"),
                                                    fg_color="#F8F4F4",
                                                    hover_color="#ECECEC",
                                                    corner_radius=5,
                                                    width=175,
                                                    height=40,
                                                    anchor="w",
                                                    image=customtkinter.CTkImage(light_image=shopICO, size=(32,32)),
                                                    compound="left",
                                                    command=self.EVENT_LOADSHOP
                                                    )

        LFrameShopButton.place(x=15,y=450)   

        print("[OK] LOADED MAIN UI")
        self.MainUi.mainloop()


if __name__ == "__main__":
    AppCall = MarketUi()
    AppCall.LoginUi.mainloop()
