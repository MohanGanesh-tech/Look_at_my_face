using System.Collections;
using System.Collections.Generic;
using UnityEngine;

using System.Net;
using System.Net.Sockets;
using System.Text.RegularExpressions;
using System.Text;

public class lookatmyface : MonoBehaviour
{

    public int portNum = 55555;
    static UdpClient udpClient;

    // Start is called before the first frame update
    void Start()
    {
        udpClient = new UdpClient(portNum);
        transform.Translate(0.0f, 2.3f, 7.5f);
    }

    // Update is called once per frame
    void Update()
    {
        IPEndPoint remoteEP = null;
        byte[] data = udpClient.Receive(ref remoteEP);
        string message = Encoding.ASCII.GetString(data);
        string[] xy = message.Split(',');
        float x = float.Parse(xy[0]);
        float y = float.Parse(xy[1]);
        print(x);
        print(y);

        //transform.Translate(x/100f, y/100f, 0f);

        transform.position = new Vector3(x, 2+y, 7.5f);

    }
}
