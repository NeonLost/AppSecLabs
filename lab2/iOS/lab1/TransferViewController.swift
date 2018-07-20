//
//  TransferViewController.swift
//  lab1
//
//  Created by n.islamov on 07.06.18.
//  Copyright © 2018 tinkoff. All rights reserved.
//

import UIKit
import Alamofire

class TransferViewController: UIViewController, UIPickerViewDelegate, UIPickerViewDataSource  {
    
    @IBOutlet weak var status: UILabel!
    @IBOutlet weak var helloUser: UILabel!
    @IBOutlet weak var fromPickerView: UIPickerView!
    @IBOutlet weak var toPickerView: UIPickerView!
    @IBOutlet weak var amount: UITextField!
    
    var token:String = ""
    var info:NSDictionary = [:]
    var cards = [NSDictionary]()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        fromPickerView.delegate = self
        fromPickerView.dataSource = self
        toPickerView.delegate = self
        toPickerView.dataSource = self

        self.updateUI()
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    @IBAction func onTransferButtonClick(_ sender: Any) {
        let fromCard = cards[self.fromPickerView.selectedRow(inComponent: 0)]
        let fromCid = fromCard.object(forKey: "cid") as! String
        let toCard = cards[self.toPickerView.selectedRow(inComponent: 0)]
        let toCid = toCard.object(forKey: "cid") as! String
        
        let params: [String: String] = [
            "token": self.token,
            "from": fromCid,
            "to": toCid,
            "amount": self.amount.text!
        ];
        Alamofire.request("http://localhost:5000/lab2/transfer", method: .post, parameters: params)
            .responseJSON { response in
                if let result = response.result.value {
                    let json = result as! NSDictionary
                    if json.object(forKey: "error") != nil {
                        let error = json.object(forKey: "error") as! String
                        self.status.text = error
                    } else {
                        let info = json.object(forKey: "info") as! String
                        self.status.text = info
                        self.updateUI()
                    }
                }
        }
    }
    
    func updateUI() {
        self.status.text = ""
        self.helloUser.text = ""
        self.amount.text = ""
        
        let params: [String: String] = ["token": self.token];
        Alamofire.request("http://localhost:5000/lab2/info", method: .post, parameters: params)
            .responseJSON { response in
                if let result = response.result.value {
                    let json = result as! NSDictionary
                    if json.object(forKey: "error") != nil {
                        let error = json.object(forKey: "error") as! String
                        self.status.text = error
                    } else {
                        self.info = json.object(forKey: "info") as! NSDictionary
                        let login = self.info.object(forKey: "login") as! String
                        self.helloUser.text = "Hello, " + login
                        
                        self.cards.removeAll()
                        self.cards.append(self.info.object(forKey: "debit") as! NSDictionary)
                        self.cards.append(self.info.object(forKey: "credit") as! NSDictionary)
                        
                        self.fromPickerView.reloadAllComponents()
                        self.toPickerView.reloadAllComponents()
                    }
                }
        }
    }
    
    @IBAction func onBackClick(_ sender: Any) {
       self.dismiss(animated: true)
    }
    
    func numberOfComponents(in pickerView: UIPickerView) -> Int {
        return 1
    }
    
    func pickerView(_ pickerView: UIPickerView, numberOfRowsInComponent component: Int) -> Int {
        return self.cards.count
    }
    
    func pickerView(_ pickerView: UIPickerView, titleForRow row: Int, forComponent component: Int) -> String? {
        let card = self.cards[row]
        let pan = card.object(forKey: "pan") as! String
        let amount = String(card.object(forKey: "amount") as! Int)
        return amount + "$" + "  " + pan
    }
}
