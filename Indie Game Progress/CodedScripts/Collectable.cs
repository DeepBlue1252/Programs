using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Collectable : MonoBehaviour
{
    public int worth = 1; 
    
    void OnTriggerEnter(Collider other)
        {
            if (other.tag == "Player")
                {
                    AttributeManager attributeManager = other.GetComponent<AttributeManager>();
                    if (attributeManager != null)
                    {
                        other.GetComponent<AttributeManager>().addGold(worth);
                        Destroy(gameObject, 0f);
                    }
                } 
        }

    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
