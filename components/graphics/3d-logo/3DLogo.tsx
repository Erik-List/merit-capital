"use client";

import { Suspense, useLayoutEffect, useRef } from "react";
import { useGLTF, OrbitControls, MeshTransmissionMaterial, useTexture } from "@react-three/drei";
import * as THREE from "three";
import { Canvas } from "@react-three/fiber";

export default function Logo3D() {
  return (
    <div className="w-full h-full relative">
      {/* 3D Canvas */}
      <Canvas 
        camera={{ position: [0, 0, 5], fov: 75 }}
        gl={{ powerPreference: 'high-performance', alpha: true }}
        className="absolute inset-0"
        style={{ zIndex: 1 }}
      >
        <Suspense fallback={null}>
          {/* Soft fill lights to avoid harsh dark bands */}
          <hemisphereLight color="#ffffff" groundColor="#8a8a8a" intensity={0.8} />
          <ambientLight intensity={0.25} />
          <Model />
          <OrbitControls 
            target={[0, 0, 0]}
            enableZoom={false}
            enablePan={false}
            autoRotate={true}
            autoRotateSpeed={-3}
            enableDamping={true}
            dampingFactor={0.05}
          />
        </Suspense>
      </Canvas>
    </div>
  );
}

export function Model(props: any) {
  const { nodes } = useGLTF('/models/merit-capital-3d.glb') as any
  // Use the same photo as a background texture for realistic transmission blur
  const bgTex = useTexture('/backgrounds/validation/bg-validation-blue-sky-peak.jpg')
  const meshRef = useRef<THREE.Mesh>(null)

  useLayoutEffect(() => {
    const mesh = meshRef.current as any
    if (!mesh) return
    const geometry: THREE.BufferGeometry | undefined = mesh.geometry
    if (!geometry) return
    geometry.computeBoundingBox()
    const box = geometry.boundingBox
    if (!box) return
    const center = new THREE.Vector3()
    box.getCenter(center)
    mesh.position.sub(center) // shift so local origin is at geometry center
  }, [])
  return (
    <group {...props} dispose={null} scale={0.7}>
      <mesh ref={meshRef} geometry={nodes.Curve004.geometry}>
        <MeshTransmissionMaterial
          background={bgTex}
          transmission={1.0}
          roughness={0.2}
          thickness={0.3}
          ior={1.4}
          envMapIntensity={1}
          samples={8}
          resolution={256}
          transparent
        />
      </mesh>
    </group>
  )
}

useGLTF.preload('/models/merit-capital-3d.glb')


