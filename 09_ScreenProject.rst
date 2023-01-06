******************
Screen Projection
******************
Blender has a screen projection function in the texture drawing mode of objects, but it is not particularly convenient to use. 
ACPainter has improved the screen projection function based on its own layer system. In addition to the original functions, 
it has added many additional useful functions, even It can be used as a simple 3D instant window baking function.

Improved Screen Projection 
========================================
1. The captured screen range conforms to the size of the 3D window screen, and the main objects in the captured screen are no longer confused by the proportion of the size.
2. When projecting an image to an object, it will detect the projectable layer, greatly reducing the failure rate of projecting an image.
3. It can be used in object mode, which is convenient and fast.

.. figure:: images/Screen_Project_001.png
   :alt: Screen_Project_001.png
   :align: center
   :width: 500px 

   3D Viewport range

.. figure:: images/Screen_Project_002.png
   :alt: Screen_Project_002.png
   :align: center
   :width: 500px 

   Blender default screen capture range

.. figure:: images/Screen_Project_003.png
   :alt: Screen_Project_003.png
   :align: center
   :width: 500px 

   ACPainter improved screen capture range   

Screen Self-Projection
==================================
The screen self-projection function is convenient for projecting any image in the 3D window to the ACPainter layer, including 
Eevee's screen post-production effects can also be captured. Here is a simple example:


.. figure:: images/Screen_Project_Self_001.png
   :alt: Screen_Project_Self_001.png
   :align: center
   :width: 500px 

   Set materials and position of the monkey head model

.. figure:: images/Screen_Project_Self_002.png
   :alt: Screen_Project_Self_002.png
   :align: center
   :width: 500px 

   Rotate 3D Viewport to a suitable angle.

.. figure:: images/Screen_Project_Self_003.png
   :alt: Screen_Project_Self_003.png
   :align: center
   :width: 500px 

   The image of the monkey head is projected onto the layer.

.. figure:: images/Screen_Project_Self_004.png
   :alt: Screen_Project_Self_004.png
   :align: center
   :width: 300px 

   turns off the self-projection object display, and only objects outside the self-projection object can be projected.

.. figure:: images/Screen_Project_Self_005.png
   :alt: Screen_Project_Self_005.png
   :align: center
   :width: 500px 

   The layer only has the projection data of objects other than its own object.

Screen Panoramic Projection
===========================
Screen panoramic projection uses six orthogonal window screen self-projection to quickly obtain the image effect in the window and project it 
on the object, which can quickly create object textures and convert material effects into textures. The following are examples of effects:

.. figure:: images/Panoramic_Project_001.png
   :alt: Panoramic_Project_001.png
   :align: center
   :width: 500px      

   Set materials and details of the model.

.. figure:: images/Panoramic_Project_002.png
   :alt: Panoramic_Project_002.png
   :align: center
   :width: 500px      

   In the free mode, add a new layer channel for Bake.

.. figure:: images/Panoramic_Project_003.png
   :alt: Panoramic_Project_003.png
   :align: center
   :width: 500px      

   Add a new layer names "ACP_Bake"

.. figure:: images/Panoramic_Project_004.png
   :alt: Panoramic_Project_004.png
   :align: center
   :width: 300px      

   Sets the screen panorama projection parameters.

.. figure:: images/Panoramic_Project_005.png
   :alt: Panoramic_Project_005.png
   :align: center
   :width: 300px      

   Press the button and wait for the completion of the screen panorama projection. After completion, there will be six layers named Front, 
   Back, Left, Right, Top, and Bottom.

.. figure:: images/Panoramic_Project_006.png
   :alt: Panoramic_Project_006.png
   :align: center
   :width: 500px

   Connect the ACP_Bake node to the material output and check the effect in the 3D Viewport. According to the characteristics and purposes of 
   the model, the order of the six layers can be adjusted to obtain the best effect. The layer seam can be removed by adding a layer mask. 

.. figure:: images/Panoramic_Project_007.png
   :alt: Panoramic_Project_007.png
   :align: center
   :width: 500px 

   Completed after simple adjustment (about 15 minutes).

For more advanced skills, see the chapter on using skills.