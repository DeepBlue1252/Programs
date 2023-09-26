using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Door : MonoBehaviour
{
    //private Animator animator;
    public float radius;
    public bool playerInInteractRange;
    public LayerMask whatIsPlayer;
    public Vector3 goesTo;
    public Transform player; 
    private Transform playerTransform;

    private void Awake()
    {
        //animator = GetComponent<Animator>();
        playerTransform = GameObject.FindGameObjectWithTag("Player").transform;
    }

    void Update()
    {
        playerInInteractRange = Physics.CheckSphere(transform.position, radius, whatIsPlayer);
        if (playerInInteractRange)
        {
            if (Input.GetKeyDown("e"))
            {
                Debug.Log(playerTransform);
                player.GetComponent<PlayerController>().Teleport(goesTo);
                //animator.SetBool("Open", true);
            }
        }
    }
}
