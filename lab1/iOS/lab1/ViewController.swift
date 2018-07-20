//
//  ViewController.swift
//  lab1
//
//  Created by n.islamov on 06.06.18.
//  Copyright © 2018 tinkoff. All rights reserved.
//

import UIKit
import Alamofire

class ViewController: UIViewController {

    @IBOutlet weak var login: UITextField!
    @IBOutlet weak var password: UITextField!
    @IBOutlet weak var status: UILabel!
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    @IBAction func onLoginClick(_ sender: Any) {
        self.status.text = ""
        
        let params: [String: String] = ["login": self.login.text!, "password": self.password.text!];
        Alamofire.request("http://localhost:5000/lab1/auth", method: .post, parameters: params)
            .responseJSON { response in
                if let result = response.result.value {
                    let json = result as! NSDictionary
                    if json.object(forKey: "error") != nil {
                        let error = json.object(forKey: "error") as! String
                        self.status.text = error
                    } else {
                        let token = json.object(forKey: "token") as! String
                        print(token)
                        
                        let storyBoard : UIStoryboard = UIStoryboard(name: "Main", bundle:nil)
                        let transferViewController = storyBoard.instantiateViewController(withIdentifier: "transferView") as! TransferViewController
                        transferViewController.token = token
                        self.present(transferViewController, animated: true, completion: nil)
                    }
                }
            }
    }
}

