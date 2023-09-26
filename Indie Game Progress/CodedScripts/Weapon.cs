using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Weapon : MonoBehaviour
{
    [Header("References")]
    [SerializeField] WeaponData weaponData;

    public GameObject player;

    void OnTriggerEnter(Collider other)
    {
        //Debug.Log(other);

        if (other.tag == "Enemy")
        {
            AttributeManager attributeManager = other.GetComponent<AttributeManager>();
            if (attributeManager != null && !player.GetComponent<PlayerController>().oneHit && player.GetComponent<PlayerController>().attacking)
            {
                player.GetComponent<PlayerController>().oneHit = true;
                attributeManager.TakeDamage(player.GetComponent<AttributeManager>().Strength+weaponData.Damage);
            }
        }
    }
}
